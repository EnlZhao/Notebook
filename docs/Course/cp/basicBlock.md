# Basic Blocks and Traces

!!! think "Motivation"
    - 语义分析阶段生成的树结构必须转化为汇编或机器语言
    - 树语言的运算符被精心挑选，以匹配大多数机器的功能
    - 但是，树语言的一些方面并不完全对应于机器语言，且树语言的一些方面可能影响编译时的优化分析

## Canonical Form | 标准格式

考虑 `CJUMP` 语句，可以跳转到两个标签，但真实的机器在条件跳转指令中，如果条件为假，则会执行下一条指令。(e.g., `JZ`, `JNZ`)

- 真正的汇编指令里有 conditional jump, 在条件成立会跳转; 条件不成立的情况下就执行自己的后一条指令
- 而在 IR tree 里无论成立还是不成立，都需要跳转

=== "IR Tree"    
    ```c
        CJUMP(e, t, f)
        ...
    LABEL(t)
        if true code
    LABEL(f)
        ...
    ```
=== "Assembly"
    ```asm
        evalute e
        JZ f
        if true code
    f:



## Step I: Canonical Trees | 标准树


## Step II & III: Taming Conditional Branches | 控制流转移

