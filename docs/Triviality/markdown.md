# 部分Markdown语法

!!! note
    一些简单的markdown语法(部分语法在不同markdown编译器上有差别)

## 关于标题
1. 一级标题 使用命令：'`#`'+'`内容`'
1. 二级标题 使用命令：'`##`'+'`内容`'
2. 三级标提 使用命令：'`###`'+'`内容`'
3. 四级标题 使用命令：'`####`'+'`内容`'
4. 五级标题 使用命令：'`#####`'+'`内容`'
5. 六级标题 使用命令：'`######`'+'`内容`'


## 加粗、倾斜、下划线、删除线、标记文本

1.  **加粗** 的命令：'`**`'+'`内容`'+'`**`'(输入之后敲空格即可将两个`**`之间的内容加粗) or '`__`'+'`内容`'+'`__`'（两个下划线），两个`**`之间无空格 ，或者使用快捷键`Ctrl`+`B`
2.  _倾斜_ 的命令：'`*`'+'`内容`'+'`*`'（同样需要在结束时敲击空格）or' `_`'+'`内容`'+'`_`'（一个下划线），或者使用快捷键`Ctrl`+`I`
3. <u>下划线</u>  ：'`<u>`'+'`内容`'+'`</u>`'，或者使用快捷键`Ctrl`+`U`
4. ~~删除线~~：’`~~`‘ + 内容 + ‘`~~`’，或者使用快捷键`Shift `+` Ctrl` + `X`
5.  ==标记== ：‘`==`’ + ‘`内容`’+‘`==`’（更好用一点），或者使用`Alt` + `Ctrl` + `H`（我的不好用）


## 分割线
    使用`*** `+ `Enter` 或者 `---` + `Enter`就可以了


## 引用
    在行首使用 ' `》`'or ' `>`' + '`空格`'
> 很多`markdown`编辑器只支持 `>`



## 列表

1. 有序列表-->使用'`数字`'+'`.`'+'`空格`' 或者 使用快捷键`Shift` + `Ctrl `+` 7`
2. 无序列表-->使用'`+`'or '`-`'or '`*`'+'`空格`' 或者 使用快捷键`Shift` + `Ctrl` + `8`
   1. 示例如下：
   2. (在保留列表连续性的同时在列表中添加另一个元素，请将该元素缩进四个空格或一个制表符)
- 一级无序列表在使用`Tab`键可以进入下一级，如下空心圆圈为`*`+`space`+`tab`


## Code

1. 行内代码： 在文字块两边加上 \` 
2. 代码块
!!! example
    ``` py title="bubble_sort.py"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```
    <br>
    ```txt
        ``` py title="bubble_sort.py"
        def bubble_sort(items):
            for i in range(len(items)):
                for j in range(len(items) - 1 - i):
                    if items[j] > items[j + 1]:
                        items[j], items[j + 1] = items[j + 1], items[j]
        ```
    ```

## 图片相关

* 插入图片格式 `![图片描述](链接)`
* 居中 --- `![图片描述](链接#pic_center)` or 使用 html 语法
* 设置图片大小 --- 调整宽高: `![图片描述](链接 =100x100)` 

> 虽然但是，还是建议直接用 html , 如 `<img src="链接" width="100" height="100" alt="图片描述" align=center />`
> Typora 上述 html 代码貌似不起作用，本人使用 `<center><img src=""/></center>`

## 数学公式&符号
> 均使用`$`+`代码`+`$`+`空格`可以打出，例如 `$\alpha$`

!!! note "原地址"
    [Markdown](https://www.yuque.com/2002_08_12/triviality/fzr6b6)

