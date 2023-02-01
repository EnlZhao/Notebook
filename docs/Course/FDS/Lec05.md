# 排序

## 简单排序

!!! info "预备知识"
    `void XSort(ElementType A[], int N)`

    1. 大多数情况下，为简单起见，讨论从小到大的整数排序
    2. N是正整数
    3. 只讨论基于比较的排序（> = < 有定义）
    4. 只讨论内部排序
    5. 稳定性：任意两个相等的数据，排序前后的相对位置不发生改变
    6. 没有一种排序是任何情况下都表现最好的

* 插入排序

    !!! example "code"
        ```c
        void InsertionSort( ElementType A[], int N )
        { 
            int P, i;
            ElementType Tmp;
            for(P = 1; P < N; P++) 
            {
                Tmp = A[P];     /* 取出未排序序列中的第一个元素*/
                for(i = P; i > 0 && A[i-1] > Tmp; i--)
                    A[i] = A[i-1];  /*依次与已排序序列中元素比较并右移*/
                A[i] = Tmp;     /* 放进合适的位置 */
            }
        }
        ```
    * 最好情况: 输入 A[] 是有序的, $T(N) = O(N)$
    * 最坏情况: 输入 A[] 是逆序的, $T(N) = O(N^2)$

??? note "引申--时间复杂度下界"
    * 对于下标 i < j, 如果 A[i] > A[j], 则称 (i, j) 是一对逆序对 (inversion)
    * 冒泡和插入排序每次交换两个相邻元素都正好消去一个逆序对
        * 插入排序: $T(N, I) = O(N + I)$
        * 其中 I 是原始序列中逆序对的数量
    * 定理:
        * 任意 N 个不同元素组成的序列平均具有 $\frac{N（N-1）}{4}$ 个逆序对
        * 任何仅以交换相邻元素来排序的算法，其平均时间复杂度为 $\Omega (N^2)$ ( $\Omega$ 指的是下界)
    
    > 要提高算法效率，需要
    > * 每次消去不止一对逆序对
    > * 每次尽量交换相隔较远的元素

## 希尔排序 | Shell Sort




<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>