# Splay Trees & Amortized Analysis

## Splay Trees | 伸展树

!!! abstract "Splay Tree - Definition"
    A relatively simple date structure, known as splay tree, that guarantees that any m consecutive tree operations take at most $O(Mlog~N)$ time.

    > It means that the <u>amortized</u> time is $O(log~N)$ 
    > Any simgle operation might take $O(N)$ time

### Find

* 伸展树的核心想法是: 一个节点被访问后，通过一系列 AVL Tree 的旋转方法将它转至根节点
* 尝试单旋:
    * ![2023-02-28-20-49-07](../../Images/2023-02-28-20-49-07.png)
    * 发现 K~3~ 沉到了更底部
* 给出新的旋转方法: 
    > For any nonroot node X, denote its parent by P and grandparent by G: 
    * Case 1: P is the root ——> Rotate X and P
    * Case 2: P is not the root 
        * Zig-zag:
            ![2023-02-28-20-59-53](../../Images/2023-02-28-20-59-53.png)
        * Zig-zig:
            ![2023-02-28-21-03-17](../../Images/2023-02-28-21-03-17.png)

        > 第一个为 LR， 第二个为两次 LL
* 那么对于开始的图形，使用 Splay 得到
    ![2023-02-28-21-05-58](../../Images/2023-02-28-21-05-58.png)
    
    > Splaying not only moves the accessed node to the root, but also roughly halves the depth of most nodes on the path.

??? example "举个栗子"
    ![2023-02-28-21-08-15](../../Images/2023-02-28-21-08-15.png)

### Deletions

* Step 1: Find X (X will be at the root)
* Step 2: Remove X (There will be two subtrees $T_L$ and $T_R$ )
* Step 3: FindMax( $T_L$ ) (The largest element will be the root of $T_L$ , and has no right child)
* Step 4: Make $T_R$ the right child of the root of $T_L$ 
 
## Amortized Analysis | 摊还分析

* worst-case bound $\ge$ amortized bound $\ge$ average-case bound
* 分析方法: 
    * Aggregate analysis | 聚合分析
    * Accounting method | 核算法
    * Potential method | 势能方法 (Highest-level)

### Aggregate Analysis

Show that for all n, a sequence of n operations takes <u>worst-case</u> time $T(n)$ in total. In the worst case, the average cost, or <u>amortized cost</u> per operation is $\frac{T(n)}{n}$ 

??? example "Stack with MultiPop(int k, Stack S)"
    ```c
    Algorithm{
        while(!IsEmpty(S) $$ k > 0)
        {
            Pop(S);
            k --;
        }
    }
    ```
    * Consider a sequence of $n$ Push, Pop, and MultiPop operations on an initially empty stack. (sizeof(S) $\le n$ )
        * 
        * $T_{amortized} ~ = ~ O(n) / n ~ = ~ O(1)$


### Accounting Method

### Potential Method


<center><font face="JetBrains Mono" size=2 color=grey >图片摘自 MOOC</font></center>