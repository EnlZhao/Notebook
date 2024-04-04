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


## LR(0) 分析


## SLR 分析


## LR(1) 分析


## LALR 分析