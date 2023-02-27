---
password: 'ZJU'
---

# 数学基础

* 整除:
    * 设 a、b 均为整数，且 a != 0, 若存在整数 k 使得 b = a * k, 则称 a 整除 b, 记作 a | b
* 最大公约数 (greatest common divisor)
    * 设 a、b 为整数，且a、b中至少有一个不等于 0，令 d = gcd(a, b)，则一定存在整数 x、y 使得下式成立：a * x + b * y = d
* 素数与互素
    * 互素 (relatively prime): 对于整数 a、b, 若 gcd(a, b) = 1, 则称 a、b 互素
    * 素数相关定理: 任一整数 a(a > 0) 都能唯一分解成 a = p~1~ * p~2~ * ··· * p~t~ (p~i~ 是素数)
    * 当 a、b 互素时，一定存在整数 x、y 使得 a * x + b * y = 1 成立
* 模 (mod) 运算与同余 (congruent)
    * 同余: a、b、n 都是整数，且 n != 0, 当 a-b 是 n 的倍数时，即 a = b + n * k (k 为整数)，我们称 a、b 对于模 n 同余, 记作 a $\equiv$ b (mod n)
    * 同余相关命题:
        1. 

## 逆元(inverse)

### 加法逆元 $a + b = 0 \mod n$
    * $明文 + 密钥 \equiv 密文 \mod n$，$密文 + 密钥逆元\equiv 明文 \mod n$

### 乘法逆元 $a * b = 1 \mod n$
    
* $明文\times密钥 \equiv 密文 \mod n$，$密文\times密钥逆元\equiv 明文 \mod n$
    * 充要条件 $\gcd(a,n)=1$
    * 求法：扩展欧几里得

!!! example "求 13 模 35 的乘法逆元"
    设 13 模 35 的乘法逆元为 x, 则 13 * x 

## 拓展欧几里得

拓展欧几里得可以用来求乘法逆元，下面是一个例子：

```plaintext
例如求 13 * x ≡ 1 (mod 35)
35 = 2*13+ 9
13 = 1*9 + 4
9  = 2*4 + 1

1 = 9-(2*4) 
  = (35 - 2*13) - (2*(13-1*9))
  = 35 - 2*13 - 2*(13-1*(35-2*13))
  = 35 - 2*13 - 2*13 + 2*(35-2*13)
  = 3*35 - 8*13
所以 (-8)*13 ≡ 1 (mod 35)
又因为 -8 ≡ 27 (mod 35)
所以 13*27 ≡ 1 (mod 35)
13在模35的情况下，乘法逆元为27
```

## 裴蜀定理 gcd(x,y) = ax + by

根据欧几里得算法

```c
x = x0;
y = y0;
while(y){
	int q = y/x;
	int r = y%x;
	y = x;
	x = r;
}
```

证明，在每一轮循环中，都有

$$
\begin{aligned}
&x_i = a_{i1}x_0+b_{i1}y_0\\
&y_i = a_{i2}x_0+b_{i2}y_0\\
\end{aligned}
$$

使用数学归纳法

1. i = 1时，$x = x_0$，$y = y_0$，即$a_{i1}=1,b_{i1}=0,a_{i2}=0,b_{i2}=1$
2. i >= 1时，若i满足上述条件，则
   - $y_{i+1} = x_i = a_{i1}x_0 + b_{i1}y_0$，$a_{(i+1)2}=a_{i1},b_{(i+1)2}=b_{i1}$
   - $x_{i+1}=y_{i}\%x_{i}=(a_{i2}x_0+b_{i2}y)-k*(a_{i1}x_0+b_{i1}y_0)=(a_{i2}-ka_{i1})x_0+(b_{i2}-kb_{i1})y_0$，$a_{(i+1)1}=a_{i2}-ka_{i1}$，$b_{(i+1)1}=b_{i2}-kb_{i1}$

Q.E.D

## 中国剩余定理

设$m_1,m_2,m_3,...,m_r$两两互素，则以下同余方程组  
$x\equiv a_i\mod m_i,\ i=1,2,3,...,r$  
模$M=m_1m_2m_3...m_r$的唯一解为  
$x=\sum\limits^{r}_{i=1}a_i*M_i*(M_i^{-1}{\rm \ mod\ }m_i)\mod M$，其中$M_i=M/m_i$  
（1）先证明x为同余方程的解  
因为$M_i\equiv 0\mod m_j(i\ne j)$，所以$x\equiv a_j\mod m_j$  
（2）再证明x是唯一解  
假设上述同余方程组有两个解$0\le x_1,x_2< M$，  
则

$$  
\begin{aligned}
x_1&\equiv a_i\mod m_i\\
x_2&\equiv a_i\mod m_i\\
\to x_1-x_2&\equiv 0 \mod m_i
\end{aligned}
$$

又因为$m_1,m_2,m_3,...,m_r$两两互素，所以$x_1 = k*M+x_2$，与假设矛盾  
Q.E.D

## Euler准则

对于整数x和奇素数p，x是模p的平方剩余（$y^2\equiv x \mod p$） 的充要条件是 $x^{(p-1)/2}\equiv 1 \mod p$  

证明：  
（1）必要性  
因为gcd(x,p)=1, $y^2\equiv x\mod p$，  
所以gcd(y,p)=1  
根据费马小定理，$y^{p-1}\equiv 1 \mod p$  
所以 $x^{(p-1)/2}\equiv 1\mod p$  
（2）充分性  
不妨设$x\in Z_p$，因为$Z_p^{*}$={1,2,3,...,p-1}在模p乘法下是循环群，所以一定存在$Z_p^*$的一个生成元b，使得 $x\equiv b^i\mod p$  
因为 $x^{(p-1)/2}\equiv 1\mod p$  
所以 $b^{i(p-1)/2}=(b^{p-1})^{i/2}\equiv 1\mod p$  
又因为 $b^{p-1}\equiv 1\mod p$，所以i为偶数  
所以x模p的平方根必有整数解，其值为$\pm b^{i/2}$  
Q.E.D  
