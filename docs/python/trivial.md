# Trivial Knowledge

This is a file containing some trivial knowledge about Python.

## `:` 和 `->`

- 有时候我们会看到这样的代码：`def foo() -> int:`，这里的 `->` 代表函数的返回值类型，这是 Python 3.5 引入的新特性。
- 有时候我们会看到这样的代码：`a: int = 1`，这里的 `:` 代表变量的类型，这是 Python 3.6 引入的新特性。
- 二者都是类型提示的一部分，不会影响代码的执行。

## 链表

Python 中没有指针这一概念，相似的概念是引用。在 Python 中，我们可以通过类的方式实现链表。

```python
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用
```

```python title="插入"
def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    n1 = n0.next
    P.next = n1
    n0.next = P
```

??? note "链表典型应用"
    > 应用自 [hello algorithm](https://www.hello-algo.com/chapter_array_and_linkedlist/linked_list/#424)

    - 单向链表通常用于实现栈、队列、哈希表和图等数据结构。
        - 栈与队列：当插入和删除操作都在链表的一端进行时，它表现的特性为先进后出，对应栈；当插入操作在链表的一端进行，删除操作在链表的另一端进行，它表现的特性为先进先出，对应队列。
        - 哈希表：链式地址是解决哈希冲突的主流方案之一，在该方案中，所有冲突的元素都会被放到一个链表中。
        - 图：邻接表是表示图的一种常用方式，其中图的每个顶点都与一个链表相关联，链表中的每个元素都代表与该顶点相连的其他顶点。
    - **双向链表常用于需要快速查找前一个和后一个元素的场景。**
        - 高级数据结构：比如在红黑树、B 树中，我们需要访问节点的父节点，这可以通过在节点中保存一个指向父节点的引用来实现，类似于双向链表。
        - 浏览器历史：在网页浏览器中，当用户点击前进或后退按钮时，浏览器需要知道用户访问过的前一个和后一个网页。双向链表的特性使得这种操作变得简单。
        - **LRU 算法**：在缓存淘汰（LRU）算法中，我们需要快速找到最近最少使用的数据，以及支持快速添加和删除节点。这时候使用双向链表就非常合适。
    - <u>环形链表常用于需要周期性操作的场景，比如操作系统的资源调度。</u>
        - **时间片轮转调度算法**：在操作系统中，时间片轮转调度算法是一种常见的 CPU 调度算法，它需要对一组进程进行循环。每个进程被赋予一个时间片，当时间片用完时，CPU 将切换到下一个进程。这种循环操作可以通过环形链表来实现。
        - **数据缓冲区**：在某些数据缓冲区的实现中，也可能会使用环形链表。比如在音频、视频播放器中，数据流可能会被分成多个缓冲块并放入一个环形链表，以便实现无缝播放。

## 切片操作符 `[], [:], [::]`

??? quote
    https://blog.csdn.net/chengyq116/article/details/100145100?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-100145100-blog-131223329.235^v43^pc_blog_bottom_relevance_base5&spm=1001.2101.3001.4242.1&utm_relevant_index=3