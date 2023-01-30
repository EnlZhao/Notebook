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
    * 对于无向图的存储，用一个长度为 N(N+1)/2 的一维数组 A 存储 {G~00~, G~10~, G~11~, ···, G~n-1~ ~0~, ···, G~n-1~ ~n-1~}, 则 G~ij~ 在 A 中对应的下标是: i * (i + 1) / 2 + j
    * 对于网络，只要把 G[i][j] 的值定义为边 < v~i~, v~j~ > 的权重即可
2. 邻接表表示法 —— G[N] 为指针数组，对应矩阵每行要给链表且只存非 0 元素
   ![2023-01-30-16-55-50](../../Images/2023-01-30-16-55-50.png)
      * 对于无向图，每个边会被存储两次
      * 对于有向图，无法遍历入度，如果要查询入度可采用以下两种方法:
          * 增加逆邻接表 <br> ![2023-01-30-17-15-48](../../Images/2023-01-30-17-15-48.png)
          * 采用多重链表 <br> ![2023-01-30-17-19-04](../../Images/2023-01-30-17-19-04.png)



<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>