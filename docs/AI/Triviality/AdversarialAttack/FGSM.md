# FGSM | Fast Gradient Sign Method

!!! quote "Paper"
    [论文地址](https://arxiv.org/abs/1412.6572)

!!! abstract "特点"
    - 基于梯度的攻击方法
    - 无目标攻击
    - 无穷范数攻击
    - 白盒攻击

## 原理

- 因为白盒攻击已知模型的内部结构和参数，故最有效的白盒攻击算法即是对模型输入的梯度进行有限扰动，使扰动后的损失函数值最大化，从而使模型的输出发生改变
- 在设计神经网络时，会使用梯度下降法使 gradient 最小，而对抗攻击相反，FGSM 使梯度上升，使得损失函数最大化

具体讲，FGSM 是在白盒环境下，通过求出模型对输入的导数，然后用符号函数得到具体的梯度方向，接着乘上一个步长，得到最终的扰动值，最后将扰动值加到原始输入上，得到对抗样本，如：![](../../Images/2023-11-22-08-41-16.png)
(数学表达如下)：

$$
x^{'} = x + \epsilon \cdot sign(\nabla_x J(\theta, x, y))
$$

- $x$：原始样本
- $x^{'}$：对抗样本
- $\epsilon$：扰动值，一旦超出阈值，该对抗样本会被人眼识别出来
- $\theta$: 模型的权重参数
- $J$：损失函数
- $y$：真实标签
- $\nabla_x$: 表示对 $x$ 求偏导

## Implementation

!!! note "Pytorch 实现"
    [:fontawesome-regular-file-code: Download fgsm_tutorial.ipynb](../fgsm_tutorial.ipynb){ .md-button }

<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>