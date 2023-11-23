# 范数 | Norm

## 向量范数

> 通常在机器学习中会看到各种距离和范数，如 $||\boldsymbol{x}||$, $||\boldsymbol{X}||$, 其中 $\boldsymbol{x}$ 和 $\boldsymbol{X}$ 分别表示向量和矩阵

为方便统一，将任意向量 $\boldsymbol{x}$ 的 $l_p$ -范数定义为：$||\boldsymbol{x}||_p = (\sum_{i=1}^n|x_i|^p)^{\frac{1}{p}}$

### $l_0$ - 范数

!!! abstract
    表示向量中非零元素的个数

<center><font face="JetBrains Mono" color=grey size=18>TODO</font></center>

### $l_1$ - 范数

!!! abstract
    表示向量中各个元素绝对值之和

<center><font face="JetBrains Mono" color=grey size=18>TODO</font></center>

### $l_2$ - 范数

!!! abstract
    表示向量各个元素的平方和的平方根

<center><font face="JetBrains Mono" color=grey size=18>TODO</font></center>

### $l_{\infty}$ - 范数

!!! abstract
    表示向量中各个元素绝对值的最大值

<center><font face="JetBrains Mono" color=grey size=18>TODO</font></center>

> $l_{-\infty}$ 与其相反，表示最小值


## 矩阵范数

> 假设矩阵 $\boldsymbol{A}$ 的维度为 $m\times n$

1. 1-范数 | $||\boldsymbol{A}||_1 = \max_{1\leq j\leq n}\sum_{i=1}^m|a_{ij}|$
      - 列范和数，即所有矩阵列向量绝对值之和的最大值
2. 2-范数 ｜ $||\boldsymbol{A}||_2 = \sqrt{\lambda_{\max}(\boldsymbol{A}^T\boldsymbol{A})} = \sqrt{\max_{1\leq i\leq n} |\lambda_i|}$(其中 $\lambda_i$ 为 $\boldsymbol{A}^T\boldsymbol{A}$ 的特征值)
      - 谱范数，即矩阵 $\boldsymbol{A}^T\boldsymbol{A}$ 的最大特征值的平方根

3. $\infty$-范数 | $||\boldsymbol{A}||_{\infty} = \max_{1\leq i\leq m}\sum_{j=1}^n|a_{ij}|$
      - 行范数，即所有矩阵行向量绝对值之和的最大值
4. F-范数 | $||\boldsymbol{A}||_F = \sqrt{\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|^2} = \sqrt{tr(\boldsymbol{A}^T\boldsymbol{A})}$ (其中 $tr(\boldsymbol{A}) = a_{11} + \dots + a_{nn}$ 表示矩阵的迹)
      - Frobenius 范数，即矩阵 $\boldsymbol{A}$ 的所有元素绝对值的平方和的平方根

??? quote
    [如何通俗易懂地解释「范数」](https://zhuanlan.zhihu.com/p/26884695)