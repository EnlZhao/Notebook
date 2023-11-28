# PGD | Project Gradient Descent

!!! quote "Paper"
    [论文地址](https://arxiv.org/abs/1706.06083)

    > 论文抛出的两个问题：
    > 
    > 1. 如何生成强对抗样本？即较小的扰动即可使模型分类错误的样本
    > 2. 如何训练一个鲁棒性强的模型？

## Quick Start

公式：

$$
X^{N+1} = \Pi_{X+S}(X^N + \alpha \cdot sign(\nabla_X J(\theta, X^N, y_{true})))
$$

- $X$: 原始样本
- $X^{N+1}$：第 $N+1$ 次迭代的样本
- $\Pi_{X+S}$: 投影函数，将值投影到 $X+S$ 的 $\epsilon$ 邻域内
- $S$: 随机噪声
- $\alpha$: 控制扰动大小的参数
- $J$: 损失函数
- $\theta$: 模型参数
- $y_{true}$: 真实标签
- $sign$: 符号函数

!!! note "PGD & BIM 主要区别"
    - PGD 使用投影函数使得对抗样本与原始样本每个点的像素值差距不大于 $\epsilon$，而 BIM 则是使用裁剪函数使得对抗样本与原始样本每个点的像素值差距不大于 $\epsilon$
    - PGD 会在对抗样本攻击前在样本中随机添加噪声

??? success "Pytorch 实现"
    [:fontawesome-regular-file-code: Download PGD.ipynb Here](../PGD.ipynb){ .md-button }

## More Details



