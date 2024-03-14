# Parsing (Top-Down Parsing)

!!! abstract
    - 本节主要介绍语法分析 (Parsing) 和上下文无关文法 (Context-Free Grammar, CFG) 的基本概念
    - 和 自顶向下的语法分析方法

## 上下文无关文法 | Context-Free Grammar

!!! note
    CFG 是一种形式文法，用于描述上下文无关语言 (Context-Free Language) 的语法结构.

### CFG 简介

!!! question "问题: 如何形式化定义编程语言的语法？"

> 语法分析的目的是教会计算机判断输入合法性

例：简单计算器程序

```c
1 + 2 - 3 +     非法
1 + 2 - a       非法
1 + (2 - 3)     合法
1 2 + - 3       非法
```

!!! note "如何判定输入合法性 & 生成语法树"
    - 首先规定好合法的基本单元 (Token) —— 词法分析
    - 其次要理解算术表达式的构成
        - 大表达式可拆分为子表达式
        - 拆解过程是递归的，直至看到基本单元

    ![](../../Images/2024-03-14-15-14-44.png)

!!! info "如何构造编程语言的语法分析器"
    - 用 CFG 定义一个编程语言的语法
    - 基于 CFG 构建解析器:
        - Top-Down Parsing | 自顶向下的语法分析
        - Bottom-Up Parsing | 自底向上的语法分析
    - More about parsing:
        - Automatic paraser generation
        - Error recovery

#### CFG 的定义

上下文无关文法: 描述语言的语法结构

$$G = (T, N, P, S)$$

- $T$: 终结符集合 (Terminals), 组成串的基本符号 (Token)
    - 例：$T = \{\text{num}, +, -, (, )\}$
- $N$: 非终结符集合 (Non-terminals), 表示串的集合的语法变量 (在程序语言中通常对应于某个程序构造)
    - 例：$N = \{\text{expr}, \text{term}, \text{stmt}\}$
- $P$: 产生式集合 (Productions), $A \rightarrow a$, $A \in N$, $a \in (T \cup N)^*$
    - 头(左)部 $A$ 是一个非终结符，右部 $a$ 是一个符号串
    - 描述了一个将终结符和非终结符组合成串的方法
    - e.g. $E \rightarrow E + E$, $E \rightarrow (E)$, $E \rightarrow \text{id}$
- $S$: 开始符号 (Start symbol), $S \in N$
    - 某个被指定的非终结符号
    - 它对应的串的集合就是文法的语言

> - $T \cap N = \emptyset$
> - $T \cup N$ : 文法符号集

#### 产生式的缩写

对一组有相同左部的 $\alpha$ 产生式

$$\alpha \rightarrow \beta_1, \dots, \alpha \rightarrow \beta_n$$

可以简记为：

$$\alpha \rightarrow \beta_1 \vert \dots \vert \beta_n$$

- 读作：$\alpha$ 定义为 $\beta_1$ 或 $\dots$ 或 $\beta_n$
- $\beta_1, \dots, \beta_n$ 称为 $\alpha$ 的候选式 (Candidate)

### 推导和归约

!!! question "问题：给定文法，如何判定输入串属于文法规定的语言?"

!!! note "推导 (Derivations) 和归约 (Reductions)"
    $$\text{给定文法}~ G=(T, N, P, S)$$

    - 直接推导：把产生式看成重写规则，把符号串中的非终结符用其产生式右部的串来代替
        - 如果 $A \rightarrow \gamma \in P$, 且 $\alpha, \beta \in (T \cup N)^*$, 称串 $\alpha A \beta$ 直接推导出 $\alpha \gamma \beta$, 并记作 $\alpha A \beta \Rightarrow \alpha \gamma \beta$
    - 直接归约：如果 $\alpha A \beta \Rightarrow \alpha \gamma \beta$, 则称 $\alpha \gamma \beta$ 直接归约到 $\alpha A \beta$
    - 多步推导：如果 $\alpha_0 \Rightarrow \alpha_1$, $\alpha_1 \Rightarrow \alpha_2$, $\dots$, $\alpha_{n-1} \Rightarrow \alpha_n$, 则可以记作 $\alpha_0 \Rightarrow \alpha_1 \Rightarrow \dots \Rightarrow \alpha_n$, 称符号串 $\alpha_0$ 经过 n 步推导得到 $\alpha_n$，可简记为 $\alpha_0 \Rightarrow^n \alpha_n$
        - $\Rightarrow^+$ 表示“经过正数步推导”
        - $\Rightarrow^*$ 表示“经过零步或多步推导”

**1)** 最左推导 (Left-most Derivation)：每步代换 **最左边的非终结符**

![](../../Images/2024-03-14-19-34-46.png)

**2)** 最右推导 (Right-most Derivation)：每步代换 **最右边的非终结符**

![](../../Images/2024-03-14-19-34-58.png)

**3)** 句型、句子和语言

- 句型 (Sentence Form)：对开始符号为 $S$ 的文法 $G$, 如果 $S \Rightarrow^* \alpha$, $\alpha \infty (T \cup N)^*$, 则称 $\alpha$ 为 $G$ 的一个句型
    - 句型中既可以包含终结符，又可以包含非终结符，也能是空串
- 句子 (Sentence)：如果 $S \Rightarrow^* w$, $w \in T^*$, 则称 $w$ 为 $G$ 的一个句子
    - 句子是<u><b>不含非终结符</b></u>的句型
- 语言 (Language)：由文法 $G$ 推导出的所有句子构成的集合，记为 $L(G)$
  
$$L(G) = \{w \vert S \Rightarrow^* w, w \in T^*\}$$


??? example "例: 文法定义的句型和句子"
    - 考虑文法：$E \rightarrow E + E \vert E * E \vert (E) \vert \text{id}$
    - 存在一下推导序列：

    $$E \Rightarrow -E \Rightarrow -(E) \Rightarrow -(E + E) \Rightarrow -(\text{id} + E) \Rightarrow -(\text{id} + \text{id})$$

    - $-(\text{id} + \text{id})$ 是文法的句子
    - $-(\text{id} + E)$ 是文法的句型

**4)** 输入串的判定

!!! question "问题：给定文法，如何判定输入串属于文法规定的语言?"

根据文法规则

- 从生成语言的角度 (句子的推导 (派生)) 出发，，从开始符号可以推导出该词串
- 从识别语言的角度 (句子的归约) 出发，从词串可以归约出开始符号

??? example
    ![](../../Images/2024-03-14-19-47-12.png)

### RE 与 CFG

!!! question "问题：为什么词法和语法分析用不同形式语言?"

<b><u>比较语法分析和词法分析</u></b>

![](../../Images/2024-03-14-19-48-33.png)

回顾 [形式语言](./lexical.md/#_4), [正则语言(由正则表达式刻画)](./lexical.md/#re), [上下文无关语言](#cfg_1)

正则文法 (正则语言的形式文法刻画) 的定义:

$$G = (N, T, P, S)$$

- $N$: 非终结符集合
- $T$: 终结符集合
- $P$: 产生式 (Production) $\alpha \rightarrow \beta$ 集合
    - 右线性文法：$\alpha \rightarrow \beta$ 形如 $A \rightarrow \alpha B$ 或 $A \rightarrow \alpha$，其中 $A, B \in N$, $\alpha \in T \cup \epsilon$
    - 左线性文法：$\alpha \rightarrow \beta$ 形如 $A \rightarrow B \alpha$ 或 $A \rightarrow \alpha$
- $S$: 开始符号, $S \in N$

> 正则语言：右线性文法/左线性文法产生的所有句子的集合

- 故从文法角度考虑，正则语言和上下无关语言对 $\alpha \rightarrow \beta$ 形式的限制不同：
    - 上下无关文法：$\alpha$ 是一个非终结符号，右部是一个符号串
    - 正则文法：右线性 $\A \rightarrow \alpha B$ 或 $\A \rightarrow \alpha$，左线性 $\A \rightarrow B \alpha$ 或 $\A \rightarrow \alpha$
    - 上下文无关语言涵盖了正则语言，即每个正则语言都是一个上下文无关语言，反之不成立
- 从实用角度, 正则语言表达能力有限，难以刻画编程语言的语法
    - 如: 不能用于描述配对或嵌套的结构
        - 例：配对括号串的集合，如不能表达 $(^n)^n, ~n\ge 1$
        - 原因：有穷自动机无法记录访问同一状态的次数

??? question "为什么词法分析用正则表达式，不用正则文法？"
    ![](../../Images/2024-03-14-20-00-54.png)

!!! note "分离词法分析和语法分析"
    - 为什么用正则语言定义词法
        - 词法规则非常简单，不必用上下文无关文法
        - 对于 Token，正则表达式描述简洁且易于理解– 从正则表达式构造出的词法分析器效率高
    - 分离词法分析和语法分析的好处
        - 简化设计、提升性能
        - 编译器的可移植性加强
        - 便于编译器前端的模块划分

??? info "引申: 形式文法的分类"
    形式语言的文法分为 4 类：

    $$\text{文法} ~ G = (T, N, P, S)$$

    - 0 型文法 (短语结构文法): 递归可枚举语言
        - $\alpha \rightarrow \beta$, $\alpha, \beta \in (T \cup N)^*$, $\vert \alpha \vert \ge 1$
    - 1 型文法 (上下文有关文法)
        - $\vert \alpha \vert \le \vert \beta \vert$, 但 $S \rightarrow \epsilon$ 可以例外
    - 2 型文法 (上下文无关文法)
        - $A \rightarrow B$, $A \in N$, $B \in (T \cup N)^*$
    - 3 型文法 (正则文法)

??? info "引申: CFG 只能表达“语法”吗？"
    ![](../../Images/2024-03-14-20-14-16.png)

## 语法分析概述 | Parsing

### CFG 的 Parse Tree

回顾 [推导和归约](#_2) 中输入串的判定

分析树 (Parse Tree) 可以看作是推导的图形化表示，其具有下面的性质：

- 根节点为文法的初始符号
- 每个叶子节点是一个终结符
- 每个内部节点是一个非终结符
- 每一个父节点和他的子节点构成一条产生式

![](../../Images/2024-03-14-20-27-09.png)

可以将语法分析看作搜索问题，语法分析的核心问题就是：对于一个终结符号串 $x$, 设法从 $S$ 推导出 $x$ 或者从 $x$ 归约出 $S$

- 自顶向下 (Top-down) 分析
    - 从开始符号 $S$ 出发，尝试根据产生式规则推导 (derive) 出 $x$
    - Parse Tree 的构造方法：从根部开始
- 自底向上(Bottom-up) 分析
    - 尝试根据产生式规则归约 (reduce) 到文法的开始符号 $S$ 
    - Parse Tree 的构造方法: 从叶子开始



### 设计编程语言的文法

## 自顶向下的语法分析 | Top-Down Parsing

