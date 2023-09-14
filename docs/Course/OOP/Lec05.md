---
date: 2023-05-03 20:11
---

# Key Words | 关键字

## `Const`

* declares a *variable* to have a constant value
* Constants are variables
    * Observe scoping rules
    * Declared with "const" type modifier
* A const in C++ defaults to internal linkage
    * the compiler tries to avoid creating storage for a const -- holds the value in its symbol table
    * extern forces storage to be allocated
* Compile time constants
    * `const int bufsize = 1024;`
    * value must be initialized
    * unless you make an explict extern declaration: `extern const int bufsize;`
    * Compiler won't let you change it
    * Compile time constants are entries in compiler symbol table, not really variables
* Run-time constants
    * const value can be expolited
    === "RIGHT"
        ``` c++
        const int size = 10;
        int finalGrade[size];   // ok
        ```
    === "WRONG"
        ``` c++
        int x;
        cin >> x;
        const int size = x;
        int finalGrade[size];   // error!
        ```

* Aggregates
    * It's possible to use **const** for aggregates, but storage will allocated. In these situations, **const** means "read-only". However, the value cannot be used at compile time because the compiler is not required to know the contents of the storage at compile time.
* Pointers and const -- a pointer may be const
    * `char * const p = "abc";` -- `p` is a const pointer to char
        * `*q = 'c';` -- ok
        * `q++;` -- error
    * `const char * p = "abc";` -- `*p` is a const char
        * `*p = 'c';` -- error
        * 指针可变（指向别人），指针所指向的内存也可变，不能做的是通过这个指针改变指向内存的值
    * `char const * p = "abc";` -- same as above `const char * p = "abc";`

    ??? example
        ``` c++
        int * ip;
        const int * cip;

        int i;
        ip = &i;    // ok
        cip = &i;   // ok, but can't use cip to change i

        const int ci = 3;
        ip = &ci;   // error, ip is not const but ci is
        cip = &ci;  // ok , both cip and ci is const
        ```

* String Literals
    * `char *s = "Hello";`
    * `s` is a pointer initialized to point to a string constant
    * This is actually a `const char *s`, but compiler accepts it
    * Don't try to change the character (it is undefined behavior)
    * If you want to change the string, put it in an array -- `char s[] = "Hello";` 
* const object
    * `const Currency price(3, 50);`
    * 此时，编译器会制止修改 `price` 中 public 成员变量以及调用 `price` 中修改成员变量函数的操作

    ???+ question "编译器怎么知道调用了会修改成员变量的函数 (非 inline)"
        * 引入新机制 - declare member functions as const

        ``` c++
        int Date::set_day(int d) 
        {
            // ... error check d here
            day = d;    // ok, non-const so can modify
        }

        int Date::get_day() const
        {
            day ++;    // ERROR modifies data member
            set_day(1); // ERROR calls non-const function

            return day; // ok, doesn't modify anything
        }
        ```
        
        * <u>此时若 Date 类的对象为 const，那么该对象不能调用除 const、static 之外的类的成员函数，否则会报错</u>
        * <u>成员函数声明尾部带有 const，那么只能调用带有 const 的成员函数且无法修改成员函数等</u>
        * Const member function usage
            * Repeat the `const` keyword in the function declaration and definition if the function is defined outside the class definition
            * `int get_day() const;` & `int Date::get_day() const { ... }`
        * Function members that do not modify the object should be declared const
        * const member functions are safe for const objects

    ???+ info "const member functions can be overloaded"
        ???+ inline end example "code"
            ``` c++
            ···
            class Date
            {
                public:
                    int get_day() const { cout << "const" << endl; }
                    int get_day() { cout << "non-const" << endl; }
            };
            int main()
            {
                Date a;
                const Date b;
                a.get_day();    // print -> "non-const"
                b.get_day();    // print -> "const"
            }
            ```
        
        * `int get_day() const;` & `int get_day();`
        * `const` is part of the function signature
        * As the code showed right, when coming across member functions with same name and arguments, `const` object will call `const` member function, non-`const` object will call non-`const` member function
        * `get_day()` & `get_day() const` 看起来没有参数，实际有隐藏参数
            * `int get_day()` -> `int get_day(Date *this)`
            * `int get_day() const` -> `int get_day(const Date *this)`
        * 编译器就可通过 `this` 来判断

* Constant in class
    * `const` object's member variable (**non-const**) must be initialized in **constructor** or **initializer list** (即你认为这个对象不可改变，但这个对象里面的变量起码要有个值)
    * if the member variable is a const
        * must be initialized in the initializer list
        * or directly initialized in the class definition (for  c++11 and later) -> `const int a = 1;`

## `static`

!!! note "Static in C++"
    * Two basic meanings
        * Static storage duration
            * allocated once at a fixed address
        * Visibility of a name
            * internal linkage
        * Don't use except inside functions and classes

=== "code"
    ``` c++
    class A
    {
        const int a;    
    public:
        A() :a(0) 
        {
            cout << "A() called" << endl;
        }
    };

    void f()
    {
        cout << "in f()" << endl;
        static A a;
        cout << "out f()" << endl;
    }
    int main()
    {
        cout << "in main()" << endl;
        f();
        cout << " ------------ " << endl;
        f();
        cout << "out main()" << endl;
        return 0;
    }
    ```
=== "output"
    ```bash
    in main()
    in f()
    A() called
    out f()
     ------------ 
    in f()
    out f()
    out main()
    ```

* 只有进入 f 函数时，才会调用 A 的构造函数，且只调用一次 (static 的存储地址不在栈中而在全局中)
* Static applied to objects
    * Constructor occurs when definition is encountered
        * Constructor is called only once
        * The constructor arguments must be satisfied
    * Destruction take place on exit from the program
        * Compiler assures LIFO order of destruction

    ??? info "Conditional construction"
        === "example"
            ```  c++
            void f(int x)
            {
                if(x > 10)
                {
                    static X my_X(x,  x * 21);
                    ···
                }
            }
            ```
        
        === "explanation"
            * `my_X` is constructed once, if `f()` is ever called with `x > 10`
            * retains its value
            * destroyed only if constructed

    ??? tip
        * avoid non-local static dependencies
        * Put static object definitions in a single file in correct order

### ==Static members==

??? question "Can we apply static to members"
    * Static means "Hidden" & "Persistent"
    * Hidden: A static member is a member (obey usual access rules)
    * Persistent: Independent of instances
    * 静态成员变量类似静态本地变量，是全局变量，访问限制于类中
    * 静态成员函数是只能访问静态成员变量的函数，不能访问非静态成员变量


* Static member variables
    * Global to all class member functions
    * *Initialized once, at file scope*
    * provide a place for this variable and init it in `.cpp`
    * No `static` in `.cpp`

??? example
    === "StatMem.h"
        ```c++
        #ifndef _STAT_MEM_
        #define _STAT_MEM_
        class StatMem{
        public:
            int getHeight() { return m_h; }
            void setHeight(int i) { m_h = i; }
            int getWeight() { return m_w; }
            void setWeight(int i) { m_w = i; }

            static int m_h;
            int m_w;
        };
        #endif
        ```
    
    === "StatMem.cpp"
        ```c++ hl_lines="5"
        #include "StatMem.h"
        #include <iostream>
        using namespace std;

        int StatMem::m_h;   // 一个静态的成员变量一定要在对应的 cpp 文件中放一个全局的定义

        int main()
        {
            StatMem sm1, sm2;
            int i = 0;
            cout << sizeof(i) << endl;
            cout << "i=" << i << endl;

            sm1.setHeight(10);
            cout << sm2.getHeight() << endl;
            sm1.setWeight(20);
            cout << sm2.getWeight() << endl;
            cout << &sm1 << '\t' << &(sm1.m_h) << '\t' << &(sm1.m_w) << endl;
            cout << &sm2 << '\t' << &(sm2.m_h) << '\t' << &(sm2.m_w) << endl;
            cout << sizeof(StatMem) << endl;

            return 0;
        }
        ```

    === "output"
        ```bash
        4
        i=0
        10
        0   
        0x7fffbf7d5e08 0x7fffbf7d5e08 0x10d62f0f8
        0x7fffbf7d5e00 0x7fffbf7d5e00 0x10d62f0f8
        4
        ```
    
    === "explanation"
        * `m_h` is a static member variable, it is global to all class member functions | 存放在全局而不是栈中，且 `sm1` 和 `sm2` 都指向同一个 `m_h`
        * `StatMem` 中只有一个 `int` 的大小，地址相差 8 是因为 64 位的机器一个 word 占 8 个字节

* Static member functions
    * Global to all class member functions
    * *No `this` pointer*
    * Can access only static member variables
    * No `static` in `.cpp`
    * Can't be dynamicallly overriden

## Namespace

!!! abstract "Namespace"
    * Expresses a logical grouping of classes, functions, variables, etc.
    * A namespace is a scope just like a class
    * Preferred when only name encapsulation is needed

    ```c++
    namespace Math
    {
        double abs(double);
        double sqrt(double);
        int trunc(double);
        ···
    }   
    ```
    
    > 大括号后不需要有分号

* Defining namespaces | 命名空间的定义
    * Place namespace definition in include file:

    ```c++
    // Mylib.h
    namespace Mylib
    {
        void f();
        class X 
        {
        public:
            void g(); 
            ··· 
        };
        ...
    }
    ```

* Defining namespace functions | 命名空间函数的定义
    * Use normal scoping to implement functions in namespaces

    ```c++
    // Mylib.cpp
    #include "Mylib.h"
    void Mylib::f()
    {
        ···
    }
    void Mylib::X::g()
    {
        ···
    }
    ```

* Using names from a namespace | 使用命名空间中的名字
    * Use scope resolution to qualify names from a namespace
    * Can be tedious and distracting

    ```c++
    // main.cpp
    #include "Mylib.h"
    int main()
    {
        Mylib::f();
        Mylib::X x;
        x.g();
        ···
    }
    ```

* Using-Declarations | 使用声明
    * Introduces a local synonym for name
    * States in one place where a name comes from
    * Eliminates redundant scope qualification

    ```c++
    // main.cpp
    void main()
    {
        // 在 main 函数中使用 using-declaration 只对函数内部有效
        using Mylib::f;
        using Mylib::X;
        f();
        X x;
        x.g();
        ···
    }
    ```

* Using-Directives | 使用指令
    * Make all names from a namespace available
    * Can be used as a notational convenience

    ```c++
    // main.cpp
    void main()
    {
        using namespace Mylib;
        f();
        X x;
        x.g();
        ···
    }
    ```

### More details

* Ambiguities | 歧义

    === "Explanation"
        * Using-directives may create potential ambiguities
        * Using-directives only make the names available
        * Ambiguities arise only when you make calls.
        * Use scope resolution to resolve 
    === "Code"
        ```c++
        // Mylib.h
        namespace Xlib
        {
            void x();
            void y();
        }
        namespace Ylib
        {
            void y();
            void z();
        } 
        // main.cpp
        #include "Mylib.h"
        void main()
        {
            using namespace Xlib;
            using namespace Ylib;
            x(); // OK
            y(); // Ambiguous
            z(); // OK
            Xlib::y(); // OK
        }
        ```

* Namespace aliases | 命名空间别名
    
    === "Explanation"
        * Namespace names that are too short may clash
        * names that are too long are hard to work with
        * Use aliasing to create workable names
        * Aliasing can be used to version libraries

    === "Code"
        ```c++
        namespace supercalifragilistic
        {
            void f();
        }
        namespace short = supercalifragilistic;
        short::f();
        ```
    
* Namespace composition | 命名空间组合

    === "Explanation"
        * Compose new namespaces using names from other ones
        * Using-declarations can resolve potential clashes
        * Explicitly defined functions take precedence

    === "Code"
        ```c++
        #include <iostream>
        namespace first
        {
            void x();
            void y();
        }
        namespace second
        {
            void y();
            void z();
        }

        void first::x()
        {
            std::cout << "first::x()" << std::endl;
        }
        void first::y()
        {
            std::cout << "first::y()" << std::endl;
        }
        void second::y()
        {
            std::cout << "second::y()" << std::endl;
        }
        void second::z()
        {
            std::cout << "second::z()" << std::endl;
        }
        namespace mine
        {
            using namespace first;
            using namespace second;
            using first::y; // resolve clash to first::y()
            void mystuff()
            {
                x();
                y();
                z();
            }
        }

        int main()
        {
            using namespace mine;
            mystuff();
        }
        ```
        
    === "Output"
        ``` shell
        first::x()
        first::y()
        second::z()
        ```

!!! note " extern "C" "
    === "Code"
        ```c++
        extern "C" {
            #include "oldc.h"
        }
        ```
    === "Explanation"
        * `extern "C"` tells the compiler to use C linkage
        * 旧版的 C 语言中没有命名空间，直接 `#include "oldc.h"` 会导致命名冲突 （链接成汇编，函数名不会加 `_`）
        * 对于新的 C++ 语言，`#include "newc.h"` 会自动加上 `_`，所以不会有命名冲突
        * 故在使用旧版 C 语言的头文件时，需要加上 `extern "C"`，告诉编译器使用 C 语言的链接方式
    === "Quote"
        [关于 C++ 中的 extern "C"](https://zhuanlan.zhihu.com/p/123269132)


* Namespace selection | 命名空间选择
    * Compose namespaces by selecting a few features from other namespaces
    * Choose only the names you want rather than all
    * Changes to "orig" declaration become reflected in "mine"

    ```c++
    namespace mine{
        using orig::Cat;    // Use Cat class from orig
        void x();           
        void y();           
    }
    ```

* Namespaces are open | 命名空间是开放的
    * Multiple namespace declarations add to the same namespace
    > Namespace can be distributed across multiple files

    ```c++
    // header1.h
    namespace X{
        void f();
    }
    // header2.h
    namespace X{
        void g();   // X now contains f() and g()
    }
    ```