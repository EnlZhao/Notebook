# CMake Note

> `CMakeLists.txt`

## 单个源文件

> 只有一个源文件 `main.c`

```makefile
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.6)
# 项目信息
project (Example1)
# 指定生成目标
add_exectutable(Example main.c)
```

* CMake 中的命令是不区分大小写的，命令由命令名称、小括号和参数组成 (参数之间使用空格进行间隔)
* 对于上述 CMakeLists.txt
    * `cmake_minimum_required` : 是指定运行所需的 CMake 的最低版本
    * `project` : 参数值 `Example1` ，表示项目的名称是 `Example1`
    * `add_executable` : 表示将 main.c 源文件编译成一个名为 `Example` 的可执行文件
* 编译项目
    * 在当前目录执行 `cmake .` 得到 `Makefile` 后使用 `make` 命令得到 `Example1` 可执行文件


## 多个源文件 

1. 同一目录，多个源文件 (Assume 此时源代码所在目录为 `Example2`)
     * 假设工程目录为：
        
        ```bash
        Example2
        |
        +--- main.c
        |
        +--- Function.c
        |
        +--- Function.h
        ```
        
     * 此时 `CMakeLists.txt` 修改为
        
        ```makefile
        # CMake 最低版本号要求
        cmake_minimum_required (VERSION 2.6)
        # 项目信息
        project (Example2)
        # 指定生成目标
        add_exectutable(Example main.c Function.c)
        ```

     * 但若将所有的源文件都按照上述形式加入会很麻烦 ——> 可以使用 `aux_source_directory` 命令，该命令会查找指定目录下的所有源文件然后将结果存进指定变量名 (`aux_source_directory(<dir> <variable>)`)
     * 此时 `CMakeLists.txt` 修改为

        ```makefile
        # CMake 最低版本号要求
        cmake_minimum_required (VERSION 2.6)
        # 项目信息
        project (Example2)
        # 查找当前目录下的所有源文件并将名称保存到 DIR_SRCS 变量
        aux_source_directory(. DIR_SRCS)
        # 指定生成目标
        add_exectutable(Example $(DIR_SRCS))
        ```

    ??? note "Problem"
        * 在实操中发现的问题 —— 变量无法使用
        * 例如上述 `DIR_SRCS` 变量无法使用从而报错，目前还未去解决 (采用文件名就能成功编译)

2. 多个目录，多个源文件 (此时源代码所在目录是 `Example3`)
     * 工程目录如下：
        
        ```bash
        Example3
        |
        +--- main.c
        |
        +--- math/
        	|
        	+--- Function.c
        	|
        	+--- FUnction.h
        ```

         * 此时需要分别在项目根目录 `Example3` 和 `math` 目录中各编写一个 `CMakeLists.txt`。 为方便可以先将 `math` 中的文件编译成静态库再由 `main` 函数调用
         * 根目录中的 `CMakeLists.txt`
     
                ```makefile
                # CMake 最低版本号要求
                cmake_minimum_required (VERSION 2.6)
                # 项目信息
                project (Example3)
                # 查找当前目录下的所有源文件并将名称保存到 DIR_SRCS 变量
                aux_source_directory(. DIR_SRCS)
                # 添加 math 子目录
                add_subdirectory(math)
                # 指定生成目标
                add_exectutable(Example $(DIR_SRCS))
                # 添加链接库
                target_link_libraries(Example Functions)
                ```

             *   `add_subdirectory(math)` 指明本项目包含一个子目录 `math` ，此时 `math` 中的 `CMakeLists.txt` 和源代码也会被处理
             *   `target_link_libraries` 指明可执行文件 `main` 需要链接一个名为 `Functions` 的链接库

         * 子目录下的 `CMakeLists.txt`
                
                ```makefile
                # 查找当前目录下的所有源文件并将名称保存到 DIR_LIB_SRCS 变量
                aux_source_directory(. DIR_LIB_SRCS)
                # 生成链接库
                add_library (Functions $(DIR_LIB_SRCS))
                ```

             *   `add_library` 将 `math` 目录中的源文件编译成静态链接库

## 自定义编译选项

>   此时源代码所在目录是 `Example4`

<center><font face="JetBrains Mono" color=grey size=18>To Be Continued</font></center>