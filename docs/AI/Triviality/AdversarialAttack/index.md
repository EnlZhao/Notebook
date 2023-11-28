# Adversarial Attack | 对抗攻击

## 什么是对抗攻击

??? info "对抗样本"
    对抗样本是指在原始样本中添加了一些扰动，使得原始样本被误分类的样本。（这样的扰动不会影响人类的识别，但可以有效使模型产生误判）

由于机器学习算法的输入形式是一种数值型向量 (numeric vector), 因此通过设计一种针对性的数值型向量，可以使得机器学习算法产生误判。这种对模型进行攻击的方式称为 **对抗攻击** (adversarial attack)

## 对抗攻击的分类

1. 从攻击环境划分：
      - 黑盒攻击：攻击者对模型的结构和参数一无所知，只能通过传入样本和观察输出结果来进行攻击
      - 白盒攻击：攻击者对模型的结构和参数完全了解
      - 灰盒攻击：攻击者对模型的结构和参数仅了解一部分
2. 从攻击目的划分：
      - 无目标攻击：如在图像分类中，只需要使得模型产生误判即可
      - 有目标攻击：如在图像分类中，需要使得模型将图像误判为某一特定类别
3. 从扰动强度划分：
      - 无穷范数攻击：
      - 二范数攻击：
      - 0 范数攻击：
4. 从攻击实现划分：
      - 基于梯度的攻击：[FGSM(Fast Gradient Sign Method)](FGSM.md)、[BIM(Basic Iterative Method)](BIM.md)、[ILCM(Iterative Least-likely Class Method)](BIM.md#info-ilcm)、[PGD(Projected Gradient Descent)](PGD.md)、MIM(Momentum Iterative Method) ...
      - 基于优化的攻击: CW(Carlini & Wagner) ...
      - 基于决策树的攻击: DEEPFOOL ...
      - ...

<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>