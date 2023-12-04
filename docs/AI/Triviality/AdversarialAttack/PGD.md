# PGD | Project Gradient Descent

!!! quote "Paper"
    [论文地址](https://arxiv.org/abs/1706.06083)

    > 论文抛出的两个问题：
    > 
    > 1. 如何生成强对抗样本？即较小的扰动即可使模型分类错误的样本
    > 2. 如何训练一个鲁棒性强的模型？

!!! info
    论文中提到：PGD 是最强的一阶攻击. 

    - 通过 PGD 发现的局部最大值在正常训练的网络和对抗训练的网络中都有着相似的损失值；
    - 即 PGD 训练对抗样本，和普通网络训练干净样本的损失是类似的；
    - 即只要能够防御住 PGD，就会对所有的一阶攻击具有鲁棒性

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

<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>