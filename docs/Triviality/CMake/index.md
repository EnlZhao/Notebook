# CMake

!!! abstract
    * 之前只了解过一点点 Makefile。 由于要用它来部署自己 VSCode 的项目等，于是浅浅记录一下学 CMake 的过程
    * 由于学习时间段，笔记不会很系统，主要针对可以成功链接自己的项目
<!-->
!!! note "注意"
    - <u>目录支持多级，但要注意当其所处位置不是最后一级（即其有子类的时候，其后不能跟有文件路径）</u>
    - 如下面第五行至第八行，后面都不能跟有文件路径，否则会报错

    ``` yaml linenums="1"
    nav:
    - Home: index.md
    - About: about.md
        - 你好: About/hello.md
    - Courses:
        - index1: 
          - index2:
            - index3:
              - file: Courses/index1/index2/index3/file.md
        - Courses: Courses/index.md #一般在文件夹下建立一个 index.md，并用同名来声明，可以表示这个文件夹的介绍
        - course1: 
            - courses1: Courses/course1/index.md
            - Lec01: Courses/course1/Lec01.md
        - course2:
            - courses2: Courses/course2/index.md
            - Lec01: Courses/course2/Lec01.md
    ```
-->
<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>
