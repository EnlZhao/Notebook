# LLM 精度原理与量化部署实战指南 (Ubuntu 20.04)

!!! abstract "📝 文档摘要"
    本文档深入解析 LLM 数值精度（FP16, BF16, FP8, INT4/NF4），对比主流成量化算法（AWQ, GPTQ, Bitsandbytes），并提供在 Ubuntu 20.04 服务器上针对 DeepSeek 系列模型进行 **AutoAWQ 量化** 与 **vLLM 高性能部署** 的完整实战代码。

    **适用环境**：Ubuntu 20.04 LTS, CUDA 12.1+, NVIDIA Ampere/Ada GPU。

---

## 第一部分：深度解析数值精度

在大模型中，"精度"决定了显存占用、计算吞吐量以及模型的推理质量。

### 1. 浮点数家族 (Floating Point)

浮点数遵循 $Value = (-1)^{S} \times 2^{E - Bias} \times (1.M)$ 的通用公式。

| 精度格式 | 总位数 | 符号位 (S) | 指数位 (E) | 尾数位 (M) | 详解与适用场景 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **FP32** | 32 | 1 | 8 | 23 | **单精度**。训练基准，精度极高但显存占用巨大（4GB/1B参数）。除科学计算外，现代 LLM 推理几乎不使用。 |
| **FP16** | 16 | 1 | 5 | 10 | **半精度**。传统推理标准。**缺点**：指数位少，动态范围窄，易出现下溢/上溢，训练需 Loss Scaling。 |
| **BF16** | 16 | 1 | 8 | 7 | **Brain Float 16**。**特点**：指数位与 FP32 相同（8位），训练极稳定。**硬件要求**：NVIDIA Ampere (A100, RTX 3090) 及以上。 |

### FP8：新一代高效格式

DeepSeek-V3 等新模型训练时大量采用 FP8。FP8 分为两个变种：

=== "E4M3 (精度优先)"
    * **结构**: 1位符号，**4位指数**，**3位尾数**。
    * **特点**: 精度较高，动态范围较小。
    * **用途**: 通常用于存储**权重 (Weights)** 和前向传播中的**激活值 (Activations)**。
    * **硬件**: 仅支持 NVIDIA Ada Lovelace (RTX 4090/6000 Ada) 和 Hopper (H100) 架构。Ampere (3090/A100) **不支持**原生 FP8 计算。

=== "E5M2 (范围优先)"
    * **结构**: 1位符号，**5位指数**，**2位尾数**。
    * **特点**: 动态范围大（类似截断的 FP16）。
    * **用途**: 通常用于反向传播中的**梯度 (Gradients)** 计算。

### 整数与非线性量化 (Integer & NF4)

* **INT8**: 线性映射 $X_{real} = Scale \times (X_{int} - ZeroPoint)$。痛点是难处理激活值的"离群点" (Outliers)。
* **NF4 (4-bit NormalFloat)**: QLoRA 提出的**非均匀量化**。利用权重服从正态分布的特性，按分位数分配量化格点，重构误差理论最优。

---

## 量化算法选型

| 算法 | 全称 | 原理 | 实验室建议 |
| :--- | :--- | :--- | :--- |
| **Bitsandbytes (BnB)** | On-the-fly | **运行时量化**。加载 FP16 模型到内存，实时压缩为 NF4/INT8。 | **实验/微调首选**。适合 QLoRA。推理速度较慢（需反量化计算）。 |
| **GPTQ** | Post-Training | **训练后量化**。基于二阶导数（Hessian）逐层量化。 | **老牌稳定**。但 4-bit 下精度保护不如 AWQ。 |
| **AWQ** | Activation-aware | **感知激活值**。保留 1% 的显著权重（Salient Weights）不量化，其余量化。 | **生产部署首选**。4-bit 精度优于 GPTQ，vLLM 支持极好。 |

---

## DeepSeek 模型量化实战 (AutoAWQ)

!!! warning "DeepSeek-V3 硬件警告"
    DeepSeek-V3 (671B) 即使在 INT4 下也需要 ~386GB 显存。单机无法量化。
    本教程以 **DeepSeek-Coder-33B** 为例，演示完整的量化流程。

### 环境配置 (Ubuntu 20.04)

```bash
# 1. 创建虚拟环境
conda create -n quantization python=3.10 -y
conda activate quantization

# 2. 安装 CUDA 兼容的 PyTorch (确保 CUDA >= 12.1)
pip install torch torchvision --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

# 3. 安装量化与推理库
pip install autoawq transformers accelerate datasets vllm
````

###  量化脚本 `quantize_deepseek.py`

此脚本执行 **Calibration (校准)** 与 **Quantization (量化)**。

```python
import torch
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

# === 配置区域 ===
MODEL_ID = "deepseek-ai/deepseek-coder-33b-instruct" # 原始模型
QUANT_PATH = "./deepseek-coder-33b-awq-4bit"         # 输出路径
QUANT_CONFIG = {
    "zero_point": True,      # 推荐 True (非对称量化，精度高)
    "q_group_size": 128,     # 标准分组大小
    "w_bit": 4,              # 4-bit 目标
    "version": "GEMM"        # 内核版本，GEMM 兼容性最好
}

def main():
    print(f"[Info] Loading model: {MODEL_ID}")
    # 加载模型 (low_cpu_mem_usage=True 对大模型至关重要)
    model = AutoAWQForCausalLM.from_pretrained(
        MODEL_ID, 
        **{"low_cpu_mem_usage": True, "use_cache": False}
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)

    print("[Info] Starting Quantization with Calibration...")
    
    # === 关键步骤：校准 ===
    # AutoAWQ 会自动下载 'pileval' 数据集进行校准
    # 这能确保量化参数适应真实的激活值分布
    model.quantize(
        tokenizer, 
        quant_config=QUANT_CONFIG,
        calib_data="pileval",  # 使用标准校准集
        max_calib_samples=128, # 样本数量
        max_calib_seq_len=512  # 序列长度
    )

    print(f"[Info] Saving quantized model to: {QUANT_PATH}")
    model.save_quantized(QUANT_PATH)
    tokenizer.save_pretrained(QUANT_PATH)
    print("[Success] Quantization Complete!")

if __name__ == "__main__":
    main()
```

---

## 第四部分：高性能部署 (vLLM)

使用 `transformers` 直接推理速度较慢。生产环境推荐使用 **vLLM**，它支持 PagedAttention 和连续批处理。

###  启动 API 服务

```bash
# 启动兼容 OpenAI 接口的服务器
# --quantization awq: 显式指定量化格式
# --gpu-memory-utilization 0.9: 充分利用显存
# --tensor-parallel-size 1: 单卡运行 (如果是 33B 模型推荐设为 2 或 4)

python -m vllm.entrypoints.openai.api_server \
    --model ./deepseek-coder-33b-awq-4bit \
    --quantization awq \
    --dtype half \
    --trust-remote-code \
    --port 8000 \
    --tensor-parallel-size 1 
```

###  客户端调用测试

```python
import requests

url = "http://localhost:8000/v1/completions"
data = {
    "model": "./deepseek-coder-33b-awq-4bit",
    "prompt": "def quick_sort(arr):",
    "max_tokens": 128,
    "temperature": 0.7
}

response = requests.post(url, json=data)
print(response.json())
```

---

## 第五部分：实验室硬件选型参考

!!! info "显存需求速查表 (基于 INT4 量化)"
- **7B 模型**: \~5 GB VRAM (单卡 3060 可跑)
- **33B 模型**: \~18 GB VRAM (单卡 3090/4090 可跑)
- **70B 模型**: \~38 GB VRAM (双卡 3090 或单卡 A6000)
- **DeepSeek-V3 (671B)**: \~380 GB VRAM (需 5x A100 80G)

!!! failure "常见报错: ValueError: check\_cuda\_libs"
如果在 Ubuntu 20.04 上运行 `bitsandbytes` 报错，通常是因为 CUDA 路径未配置。

` bash export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64  `

```
