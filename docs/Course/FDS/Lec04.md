# 图 | Graph

## Definitions

1. Length of a path: 路径上边的数目
2. Simple path: Path 中的点 v~i1~, v~i2~, ···, v~in~ 都不同
3. 无向图
      1. connected: 若存在一条从 v~i~ 到 v~j~ 的路径，则称 v~i~ 和 v~j~ 连通
      2. connected graph: 任意点之间都连通，称无向图是连通的
      3. connected component: 无向图的极大连通子图
4. tree: 连通的无环图
5. DAG: directed acyclic graph | 有向无环图 
6. Strongly connected component: 有向图的极大强连通子图
7. Degree(v): 
      1. 对有向图，度分为入度和出度
      2. 对无向图，度数是与其相邻的节点数
      3. 边数等于所有节点的度数和除以 2

## 图的表示

1. 邻接矩阵 G[N][N] —— N 个顶点从 0 到 N-1 编号
      * G[i][j] = < v~i~, v~j~ > 是 G 中的边 ? 1 : 0
        
!!! tip
    * 对于无向图的存储，用一个长度为 N(N+1)/2 的一维数组 A 存储 {G~00~, G~10~, G~11~, ···, G~(n-1)0~, ···, G~(n-1)(n-1)~}, 则 G~ij~ 在 A 中对应的下标是: i * (i + 1) / 2 + j
    * 对于网络，只要把 G[i][j] 的值定义为边 < v~i~, v~j~ > 的权重即可
2. 邻接表表示法 —— G[N] 为指针数组，对应矩阵每行要给链表且只存非 0 元素
   ![2023-01-30-16-55-50](../../Images/2023-01-30-16-55-50.png)
      * 对于无向图，每个边会被存储两次
      * 对于有向图，无法遍历入度，如果要查询入度可采用以下两种方法:
          * 增加逆邻接表 <br> ![2023-01-30-17-15-48](../../Images/2023-01-30-17-15-48.png)
          * 采用多重链表 <br> ![2023-01-30-17-19-04](../../Images/2023-01-30-17-19-04.png)

## 拓扑排序

!!! abstract
      * AOV 网络 —— 定点表示活动，边表示先后关系
      * 若存在一条从 i 到 j 的路径，则称 i 为 j  的前驱(predecessor), j 是 i 的后继(successor)
      * 若存在一条边 < i, j >，则称 i 是 j 的直接前驱(immediate predecessor)，j 是 i 的直接后继

### 拓扑序

* 若在图中从 V 到 W 有一条有向路径，则 V 一定排在 W 之前。满足此条件的顶点序列称为一个拓扑序(获得一个拓扑序的过程就是拓扑排序)
* AOV 如果有合理的拓扑序，则必定是有向无环图(Directed Acyclic Graph, DAG)
> ![2023-01-30-18-22-40](../../Images/2023-01-30-18-22-40.png)
> 如果有向图中出现环，一定不可能得到一个合理的拓扑序

### 拓扑排序算法

```c
void Topsort(Graph G)
{
      int Counter;
      Vertex V, W;
      for(Counter = 0; Counter < NUmVertex; Counter ++)
      {
            V = FindNeVertexOfDegreeZero();     /* O(|V|) */
            if(V == NotAVertex)
            {
                  Error("Graph has a cycle");
                  break;
            }
            TopNum[V] = Counter;    /*or output V*/
            for(each W adjacent to V)
                  Indegree[W] --;
      }
}
```

* 上述算法的时间复杂度 $T = O(|V|^2) $
* Improvement: 随时将入度变为 0 的顶点放到一个容器中(栈或队列等)

```c title="Improvement"
void Topsort( Graph G )
{   
      Queue  Q;
      int  Counter = 0;
      Vertex  V, W;
      Q = CreateQueue( NumVertex );  
      MakeEmpty( Q );
      for ( each vertex V )
            if ( Indegree[ V ] == 0 )   
                  Enqueue( V, Q );
      while ( !IsEmpty( Q ) )
      {
            V = Dequeue( Q );
            TopNum[ V ] = ++ Counter; /* assign next */
            for ( each W adjacent to V )
                  if ( – – Indegree[ W ] == 0 )  
                        Enqueue( W, Q );
      }  /* end-while */
      if ( Counter != NumVertex )
            Error( “Graph has a cycle” );
      
      DisposeQueue( Q ); /* free memory */}
```
> 若有环则一定会存在找不到入度为 0 的点，来进入构成环的子图

??? example "邻接表存储---拓扑排序算法"
    ```c
    bool TopSort( LGraph Graph, Vertex TopOrder[] )
    { /* 对Graph进行拓扑排序,  TopOrder[]顺序存储排序后的顶点下标 */
    int Indegree[MaxVertexNum], cnt;
    Vertex V;
    PtrToAdjVNode W;
    Queue Q = CreateQueue( Graph->Nv );
    
    /* 初始化Indegree[] */
    for (V=0; V<Graph->Nv; V++)
          Indegree[V] = 0;
          
    /* 遍历图，得到Indegree[] */
    for (V=0; V<Graph->Nv; V++)
          for (W=Graph->G[V].FirstEdge; W; W=W->Next)
                Indegree[W->AdjV]++; /* 对有向边<V, W->AdjV>累计终点的入度 */
                
    /* 将所有入度为0的顶点入列 */
    for (V=0; V<Graph->Nv; V++)
          if ( Indegree[V]==0 )
                AddQ(Q, V);
                
    /* 下面进入拓扑排序 */ 
    cnt = 0; 
    while( !IsEmpty(Q) ){
          V = DeleteQ(Q); /* 弹出一个入度为0的顶点 */
          TopOrder[cnt++] = V; /* 将之存为结果序列的下一个元素 */
          /* 对V的每个邻接点W->AdjV */
          for ( W=Graph->G[V].FirstEdge; W; W=W->Next )
                if ( --Indegree[W->AdjV] == 0 )/* 若删除V使得W->AdjV入度为0 */
                AddQ(Q, W->AdjV); /* 则该顶点入列 */ 
    } /* while结束*/
    
    if ( cnt != Graph->Nv )
          return false; /* 说明图中有回路, 返回不成功标志 */ 
    else
          return true;
    }
    ```

## 最短路算法

!!! abstract "最短路径问题的抽象"
    在网络中，求两个不同顶点之间的所有路径中，边的权值之和最小的那一条路径。这条路径即两点之间的最短路径(Shortest Path), 第一个顶点为源点(Source), 最后一个顶点为终点(Destination)

### 问题分类

1. 单源最短路径: 从固定源点出发，求其到所有其他顶点的最短路径
      1. (有向)无权图
      2. (有向)有权图
2. 多源最短路径: 求任意两顶点间的最短路径

### 无权图的单源最短路

> 按照递增(递减)的顺序找出到各顶点的最短路
> 采用 BFS(Breadth-first search)

!!! note "Implementation"
    ```c
    Table[i].Dist = distance from s to vi  /* initialized to be  except fors */
    Table[i].Known = 1 if vi is checked; or 0 if not
    Table[ i ].Path = for tracking the path   /* initialized to be 0 */
    ```
1. Normal:
```c
void Unweighted( Table T )
{   int  CurrDist;
    Vertex  V, W;
    for ( CurrDist = 0; CurrDist < NumVertex; CurrDist ++ ) {
        for ( each vertex V )
	if ( !T[ V ].Known && T[ V ].Dist == CurrDist ) {
	    T[ V ].Known = true;
	    for ( each W adjacent to V )
	        if ( T[ W ].Dist == Infinity ) {
		T[ W ].Dist = CurrDist + 1;
		T[ W ].Path = V;
	        } /* end-if Dist == Infinity */
	} /* end-if !Known && Dist == CurrDist */
    }  /* end-for CurrDist */
}
```
> $T = O(|V|^2)$ 
2. Improvement:
```c
void Unweighted( Table T )
{   /* T is initialized with the source vertex S given */
    Queue  Q;
    Vertex  V, W;
    Q = CreateQueue (NumVertex );  MakeEmpty( Q );
    Enqueue( S, Q ); /* Enqueue the source vertex */
    while ( !IsEmpty( Q ) ) {
        V = Dequeue( Q );
        T[ V ].Known = true; /* not really necessary */
        for ( each W adjacent to V )
	if ( T[ W ].Dist == Infinity ) {
	    T[ W ].Dist = T[ V ].Dist + 1;
	    T[ W ].Path = V;
	    Enqueue( W, Q );
	} /* end-if Dist == Infinity */
    } /* end-while */
    DisposeQueue( Q ); /* free memory */
}
```
> $T = O(|V|+|E|)$ 

### 有权图的单源最短路

> 按照递增的顺序找出到各顶点的最短路

#### Dijkstra 算法

* 令 S = {源点 s + 已经确定了最短路径的顶点 v~i~ }
* 对任一未收录的顶点 v, 定义 dist[v] 为 s 到 v 的最短路径长度，但该路径仅经过 s 中的顶点。
* 由于路径按照递增顺序生成
    * 真正的最短路必须只经过 S 中的顶点
    * 每次从未收录的顶点中选一个 dist 最小的收录
    * 增加一个 v 进入 S，可能影响另一个 w 的 dist 值(dist[w] = min{dist[w], dist[v] + < v, w > 的权重})

!!! example "code"
    ```c title="伪码"
    void Dijkstra(Table T)
    {
          Vertex V, W;
          for(;;)     /* O(|V|) */
          {
                V = smallest unknown distance vertex;
                if(V == NotAVertex)
                      break;
                T[V].Known = true;
                for(each W adjacent to V)
                      if(!T[W].Known)
                            if(T[V].Dist + Cvw < T[W].Dist)
                            {
                                  Decrease(T[W].Dist to T[V].Dist + Cvw);
                                  T[W].Path = V;
                            }/* end-if update W */
          }/* end-for(;;) */
    }
    /* 不能解决有负边的情况 */
    ```

    ??? example "Dijkstra算法的声明"
        ```c 
        typedef int Vertex;
        struct TableEntry
        {
              List Header;      /* Adjacency list */
              int Known;
              DistType Dist;
              Vertex Path;
        };
        /* Vertices are numbered from 0 */
        #define NotAVertex (-1)
        typedef struct TableEntry Table[NumVertex];
        ```

    ??? example "表初始化例程"
        ```c 
        void InitTable(Vertex Start, Graph G, Table T)
        {
              int i;
              ReadGraph(G, T);  /* Read graph somehow */
              for(i = 0; i < NumVertex; i++)
              {
                    T[i].Known = False;
                    T[i].Dist = Infinity;
                    T[i].Path = NotAVertex;
              }
              T[Start].dist = 0;
        }
        ```

    ??? example "显示实际最短路径的例程"
        ```c
        /* Print shortest path to V after Dijkstra has run */
        /* Assume that the path exists */
        void PrintPath(Vertex V, Table T)
        {
              if(T[V].Path != NotAVertex)
              {
                    PrintPath(T[V].Path, T);
                    printf(" to");
              }
              printf("%v", V);  // %v 是伪代码
        }
        ```
* 因为判定条件 T[V].Dist + Cvw < T[W].Dist，T[i].Dist 要初始化为正无穷
* 优化如下：
    * Implementation 1: 直接扫描所有未收录顶点 -- $O(|V|)$ 
        * $T = O(|V|^2 + |E|)$ -- 对于稠密图效果好
    * Implementation 2: 将 dist 存在最小堆中 -- $O(log|V|)$ 
        * 更新 T[W].Dist 的值 -- $O(log|V|)$ 
        * $ T = O(|V|log|V| + |E|log|V|) = O(|E|log|V|) $  -- 对稀疏图效果好(指 V 和 E 一个数量级)

#### 带负权图

时间复杂度 $T = O(|V| \times |E|)$
```c
void  WeightedNegative( Table T )
{   
    Queue  Q;
    Vertex  V, W;
    Q = CreateQueue (NumVertex );  
    MakeEmpty( Q );
    Enqueue( S, Q ); /* Enqueue the source vertex */
    while ( !IsEmpty( Q ) ) 
    {
        V = Dequeue( Q );   /* each vertex can dequeue at most |V| times */
        for ( each W adjacent to V )
            if ( T[ V ].Dist + Cvw < T[ W ].Dist )  /* no longer once per edge */
            {
                T[ W ].Dist = T[ V ].Dist + Cvw;
                T[ W ].Path = V;
                if ( W is not already in Q )
                    Enqueue( W, Q );
            } /* end-if update */
    } /* end-while */
    DisposeQueue( Q ); /* free memory */
}
/* negative-cost cycle will cause indefinite loop */
```

#### 无环图 | Acyclic Graph



## 深度优先搜索 | DFS



<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>