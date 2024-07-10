# Compile Principle | 编译原理

!!! abstract
    - 本课主要围绕 *Modern Compiler Implementation in C* , Andrew W. Appel（俗称“虎书”）
    - 课程内容对应“虎书”中的 1-11，13，14，18章
    - 课程主页：
        - https://rainoftime.github.io/teaching/
        - https://accsys.pages.zjusct.io/accipit/

    ??? note "考核方式"
        - 课程作业(课后小型练习题) = 10%
        - 随堂测验 = 10%
        - 期中考试 = 15%
        - 综合性课程设计 = 25%
        - 期末考试 = 40% 

!!! warning "Attention"
    - 基本块后面的笔记先不发了（做不完了
    - 需要的看[他(@小🐷)](https://www.yuque.com/howjul/rt9ms6/qyhhptbubm5spvta)的去

!!! success "list"
    - [x] [Introduction | 课程介绍](intro.md)
    - [x] [Lexical Analysis | 词法分析](lexical.md)
    - [x] [Parsing 1 | 语法分析](parsing1.md) (Top-Down Parsing)
    - [x] [Parsing 2 | 语法分析](parsing2.md) (Bottom-Up Parsing)
    - [x] [Semantic Analysis | 语义分析，Activation Record | 活动记录](semantic.md)
    - [x] [Translating into Intermediate Code | 中间代码生成](intermediateCode.md)
    - [ ] [Basic Blocks and Traces | 基本块与轨迹](basicBlock.md)
    - [ ] [Instruction Selection | 指令选择](instructionSel.md)
    - [ ] [Liveness Analysis | 活跃变量分析](LivenessAnalysis.md)
    - [ ] [Register Allocation | 寄存器分配](RegAlloc.md)
    - [ ] [Garbage Collection | 垃圾回收](GarbageCollection.md)
    - [ ] [Object-Oriented Languages | 面向对象语言](OOLang.md)
    - [ ] [Loop Optimization | 循环优化](LoopOptimization.md)

??? quote "More Reference"
    - [Stanford cs143](https://web.stanford.edu/class/cs143/)
    - [MIT](https://github.com/6035/sp21)
    - [UC Berkeley](https://inst.eecs.berkeley.edu/~cs164/fa21/)
    - *Compiler -- Principles, Techniques and Tools (2nd ed.)* , Aho, Sethi and Ullman（俗称“龙书”）
    - *Engineering a Compiler (2nd/3rd ed.)* , Cooper, Keith D., Torczon, Linda（俗称“橡书”）
    - *Advanced Compiler Design and Implementation* , Steven S.Muchnick（俗称“鲸书”）
    - *Parsing Techniques: A Practical Guide* ， Grune, Jacobs