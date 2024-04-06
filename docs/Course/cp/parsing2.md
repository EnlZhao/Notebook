# Parsing (Bottom-Up Parsing)

!!! note "Bottom-Up Parsing"
    - 表达力: Every LL(k) grammar is also LR(k) 
    - 被 Parser 自动生成器广泛采用 (Yacc, Bison, etc)

LR(k) parsing: 

- L: left-to-right scan of input
- R: rightmost derivation in reverse
- k: k tokens of lookahead (当 k被省略的时候, 假设为1)

!!! abstract "The Idea of Bottom-Up Parsing"
    - 自底向上的语法分析过程可以看成是从串 $w$ 归约为文法开始符号 $S$ 的过程
    - 归约步骤：一个与某产生式体相匹配的特定子串被替换为该产生式头部的非终结符号
    - 问题化为：
        - 何时归约 (归约哪些符号串) ？
        - 归约到哪个非终结符号？

## Shift-Reduce | 移入-规约

!!! abstract "Idea"
    将输入串切分成两个子串：

    - Right substring (a string of **terminals**): 还没被 parser 处理的部分
    - Left substring (a string of **terminals and non-terminals**): 已经被 parser 处理的部分

左右子串使用一个特殊符号 `｜` 分隔 (`｜` 不是字符串的一部分)，初始化时，`｜` 在最左边。

??? example
    ![](../../Images/2024-04-06-20-41-51.png)

    - 相当于最右推导的逆过程：

    $$
    \textcolor{black}{E} \Rightarrow \textcolor{black}{E} + (\textcolor{red}{E}) \Rightarrow \textcolor{red}{E} + (\textcolor{black}{int}) \Rightarrow \textcolor{black}{E} + (\textcolor{red}{E}) + (\textcolor{black}{int}) \Rightarrow \textcolor{red}{E} + (\textcolor{black}{int}) + (\textcolor{black}{int}) \Rightarrow \textcolor{black}{int} + (\textcolor{black}{int}) + (\textcolor{black}{int})
    $$

    - 如例子所示，LR 分析其实就是最右推导的逆过程，限制了规约方式

!!! note "最右句型"
    - 最右句型：最右推导过程中出现的句型
    - LR 分析的每一步都是最右句型

LR 分析的一般模式是 **基于栈的 shift-reduce**

考虑 $\alpha \vert \beta$

LR 分析有两个 component，四个 action

- Two components:
    - Stack: 保存左子串 $\alpha$ (terminals and non-terminals)
    - Input Stream: 保存右子串 $\beta$ (terminals)
- Four actions:
    - **Shift:** 将下一个输入 token (terminal) 推入栈顶
    - **Reduce:** 
        - Top of stack should match RHS (Right-Hand-Side) of rule (e.g., X -> A B C)
        - pop the RHS from the top of stack (e.g., pop C B A)
        - push the LHS onto the stack (e.g., push X)
    - **Error:**
    - **Accept:** shift $ and can reduce what remains on stack to the start symbol!

那么该何时 shift, 何时 reduce 呢？

![](../../Images/2024-04-06-20-53-49.png)

!!! success "LR 文法的关系"
    $$
    \text{LR(0)} \subset \text{SLR} \subset \text{LALR} \subset \text{LR(1)}
    $$

    即一个文法是 LR(0) 文法，那么它一定是 SLR ，以此类推

## LR(0) 分析

### LR(0) 文法的 NFA

> 具体操作和计算中不会计算 NFA，只是为了理解 LR(0) 文法的生成过程

#### 语法分析思路

LR(0) 文法就是自底向上分析：不断凑出产生式的 RHS, 然后规约为 LHS，直到规约为开始符号

???+ example
    假设下一次将会用到的产生式是：$X \rightarrow \alpha \beta$, 那么在使用它归约前，栈顶 (右侧是栈顶) 可能包含三种情况：

    1. $\dots$
    2. $\dots \alpha$
    3. $\dots \alpha \beta$

    即凑出 RHS 的进度不同

如何针对不同进度的 RHS 进行规约呢？

<u>可以维护一个状态，记录当前匹配的进度</u>

!!! success "项/Item"
    项/Item: 一个产生式加上在其中某处的一个点 `·`

    - 例如产生式 $A \rightarrow \cdot XYZ$ 有四个 Item
        - $A \rightarrow \cdot XYZ$
        - $A \rightarrow X \cdot YZ$
        - $A \rightarrow XY \cdot Z$
        - $A \rightarrow XYZ \cdot$
        - 其中 `·` 表示当前匹配的进度
        - 例如：$A \rightarrow \cdot XYZ$ 表示当前匹配/归约到了 RHS 的开头
        - $A \rightarrow X \cdot YZ$ 已经匹配/归约到了 $X$，期望在接下来的输入中经过扫描/归约得到 $YZ$，然后把 $XYZ$ 归约到 A
        - $A \rightarrow XYZ \cdot$ 表示已经匹配/归约到了 $XYZ$, 可以把 $XYZ$ 归约为 $A$
    - Item 起的作用类似于 NFA 的状态



#### 构造 NFA


### LR(0) 文法的 DFA 和分析表

## SLR 分析


## LR(1) 分析


## LALR 分析