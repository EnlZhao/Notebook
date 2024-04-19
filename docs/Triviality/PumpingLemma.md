# Pummping Lemma

!!! quote "Reference"
    - [:fontawesome-solid-link: wiki - Pummping Lemma](https://en.wikipedia.org/wiki/Pumping_lemma_for_regular_languages)

## Statement

Let $L$ be a regular language. Then there exists a number $p$ (the "pumping length") such that any string $s$ in $L$ of length at least $p$ can be divided into three pieces, $s = xyz$, satisfying the following conditions:

1. For each $i \geq 0$, the string $xy^iz$ is in $L$.
2. The length of $y$ is greater than 0.
3. The length of $xy$ is at most $p$.

意思就是说：如果一个语言 $L$ 是正则的，那么存在一个数 $p$（称为“pumping length”），使得任何长度至少为 $p$ 的字符串 $s$ 都可以被分为三部分 $s = xyz$，满足以下条件：

1. 对于任何 $i \geq 0$，字符串 $xy^iz$ 都在 $L$ 中。
2. 字符串 $y$ 的长度大于 0。
3. 字符串 $xy$ 的长度最多为 $p$。

## Proof

> TODO


## Application

假定一个语言

$$
L = \{0^n1^n | n \geq 0\}
$$

我们来证明这个语言不是正则的。

1. 假设一个字符串 $s = 0^p1^p = xyz$，其中 $|xy| \leq p$，$|y| > 0$。
2. 如果 $y$ 只包含 0，那么 $xy^2z$ 中 0 的数量会超过 1 的数量，因此 $xy^2z \notin L$。
3. 如果 $y$ 包含 1，那么 $xy^0z$ 中 0 的数量会少于 1 的数量，因此 $xy^0z \notin L$。
4. 如果 $y$ 同时包含 0 和 1，那么不满足 $|xy| \leq p$ 的条件。
5. 因此，这个语言不是正则的。
