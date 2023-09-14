---
date: 2023-05-03 20:11
---

# Object Interactive | 对象交互

## local variable

* Local variables are defined inside a method, have a scope limited to the method to which they belong

??? example 
    ```c++
    #include <iostream>
    using namespace std;
    int value = 0xdeadbeef;

    class A {
    private:
        int value;
    public:
        A():value(0xabababab) {}
        void f(){
            int value = 0xcdcdcdcd;
            cout << hex << value << endl;       // 本地变量 value -> 0xcdcdcdcd
            cout << hex << this->value << endl; // 成员变量 value -> 0xabababab
            cout << hex << ::value << endl;     // 全局变量 value -> 0xdeadbeef
        }
    };
    int main()
    {
        A a;
        a.f();
    }
    ```

## Initialization

* Member Init
    * Directly initialize a member (benefit: for all constructors)
    * Only C++11|| works

    ??? example
        ```c++
        class A{
        private:
            int A = 10;
        ···
        };
        ```

* [Initializer list](../Lec02/#initializer-list)

??? note "initialization vs. assignment"
    * `Student::Student(string s):name(s) {}`
        * initiazlization before constructor
    * `Student::Student(string s) { name = s; }`
        * assignment in constructor (在赋值前，name 已经被初始化为一个空字符串)
        * string must have a default constructor

## Function overloading | 函数重载

* Same functions with different arguments list

```c++
void print(char* str, int width);   // #1
void print(double d, int width);    // #2
void print(long l, int width);      // #3
void print(int i, int width);       // #4
void print(char *str);              // #5

print("Hello", 10);                 // #1
print(1.234, 10);                   // #2
print(123456789L, 10);              // #3
print(123456789, 10);               // #4
print("Hello");                     // #5
```

!!! note "Overload and auto-cast"
    ```c++
    ···
    void f(short i) { cout << "short" << endl; }
    void f(double d) { cout << "double" << endl; }

    int main()
    {
        f('a');       // ambiguous (char -> short or char -> double)
        f(1);         // ambiguous (int -> short or int -> double)
        f(1L);        // ambiguous (long -> short or long -> double)
        f(1.0);       // right
    }
    ···
    ```

## Default arguments

* A default argument is a value given in the declaration that the compiler automatically inserts if you don't provide a value in the function call
* To define a function with an argument list, defaults must be added **from right to left**

```c++
int a(int n, int m = 4, int j = 5);
int b(int n, int m = 4, int j); // error
int c(int n = 1, int m = 2, int j = 3); 

Ha = a(1);      // n = 1, m = 4, j = 5
Ha = a(1, 2);   // n = 1, m = 2, j = 5
```

!!! note
    默认参数要写在函数声明中，函数定义中不能重复写默认参数

## C++ access control

* The members of a class can be cataloged, marked as 
    * **public** -> means all member declarations that follow are available to everyone
    * **private** -> means that no one can access that member except inside function members of that type
    * **protected** -> 对子类有效

### Friends | 友元

* to explicitly grant access to a function that isn't a member of the structure
* The class itself controls which code has access to its members
* Can declare a global function as a **friend** , as well as a member function of another class, or even an entire class, as a **friend**
* **friend** is a declaration rather than a definition

??? example
    ```c++
    struct Y{
        void f(X*);
    };
    struct X{
    private:
        int i;
    public:
        void initialize();
        friend void g(X*, int); // Global friend
        friend void Y::f(X*);   // Struct member friend
        friend struct Z;    // Entire struct is a friend
    };
    ```

    ??? example "友元"
        === "code"
            ``` c++
            #include <iostream>
            using namespace std;

            class A;
            class B
            {
            private:
                int value;
            public:
                B():value(0x12345678){}
                void Print(A a);
            };

            //void Print(A a);

            class A 
            {
            private:
                friend void Print(A a);
                int value;
            public:
                friend void B::Print(A a);
                A():value(0xabababab){}
            };
            void B::Print(A a)
            {
                cout << "B::Print" << endl;
                cout << hex << value <<endl; // 成员变量 value -> 0x12345678
                cout << a.value << endl;     // 成员变量 value -> 0xabababab

            }
            void Print(A a)
            {
                cout << "Global Print" << endl;
                cout << a.value << endl;     // 成员变量 value -> 0xabababab
            }


            int main()
            {
                A a;
                B b;
                b.Print(a);
                Print(a);
                return 0;
            }
            ```
        === "output"
            ```shell
            B::Print
            12345678
            abababab
            Global Print
            abababab
            ```
        === "测试时的一个问题"
            * 刚开始的时候把友元函数放到 `public` 下了，一直波浪线错误
            * 后来放到 `A` 最前面就好了（不确定是出了什么问题
            * 后来又试了试放到 `A` 的任意位置都是正常可用的😰



??? quote
    [一个关于友元的十分通俗的例子](https://blog.csdn.net/weixin_46098577/article/details/116596183)

## Inline Functions

> Inline 的 body 是声明，不是定义

* In order to solve the problem that some frequently called small functions consume a large amount of stack space (stack memory), **inline** functions are introduced
* An inline function is expected in place, like a preprocessor macro, so the overhead of the function call is eliminated

```c++
inline int plusOne(int x);
inline int plusOne(int x){ return ++x; };
```

* <u>Repeat **inline** in the definition and declaration</u>
* An inline function definition may not generate any code in .obj file
* Inline functions in header file
    * So you can put inline functions' bodies in header file. Then `#include` it where the function is needed
    * Never be afraid of multi-definition of inline functions, since they have no body at all
    * Definitions of inline functions are just declarations
* Inline inside classes
    * Any function you define inside a class declaration is automatically an inline

    > 在类中使用 inline 函数，要么把主体放在 class 内，要么放在一个文件中（inline 是声明，不是定义）

    ??? example
        === "inside"
            ```c++
            class A{
            public:
                inline void f(){ } // automatically inline (`inline` can be omitted)
            };
            ```
        === "outside"
            ```c++
            class A{
            public:
                inline void f();    // `inline` can be omitted
            };
            inline void A::f(){} // OK
            ```

* Tradeoff of inline functions
    * Body of the called function is to be inserted into the caller
    * This may expand the code size
    * but deduces the overhead of calling time
    * So it gains speed at the expenses of space
    * In most cases, it is worth
    * It is much better than macro in C. It checks the type of the parameters
* Inline may not in-line
    * The compiler does not have to honor your request to make a function inline. It might decide the function is too large or notice that is calls itself(recursion is not allowed or indeed possible for inline functions), or the feature might not be implemented for your particular compiler
* Inline or not?
    * Inline:
        * Small functions
        * Frequently called functions, e.g. inside loops
    * Not Inline:
        * Very large functions
        * Recursive functions
    * A lazy way
        * Make all your functions inline
        * Never make any function inline