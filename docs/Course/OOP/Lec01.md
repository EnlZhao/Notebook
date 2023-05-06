---
date: 2023-03-03 14:00
---

# Beginning

## 第一个程序

```c++
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello World!" << endl;
}
```

* `<iostream>` 为内置类型对象提供了输入输出支持，同时也支持文件的输入输出，类的设计者可以通过对 `iostream` 库的扩展来支持自定义类型的输入输出操作
* `using namespace std;` 告诉编译器使用 std 命名空间 (命名空间是 C++ 中一个相对新的概念)
    * `namespace` 是指标识符的各种可见范围，C++ 标准程序库中的所有标识符都被定义于一个名为 std 的 `namespace` 中
    * 由于 `namespace` 的概念，使用 C++ 标准程序库的任何标识符时，可以有三种选择：
        1. 直接指定标识符 —— 如 `std::ostream` 而不是 `ostream` (完整语句 A : `std::cout << std::hex << 5.0 << std::endl;`)
        2. 使用 `using` 关键字 —— 如 `using std::cout; using std::endl` (完整语句 A 改写为: `cout << std::hex << 5.0 << endl;`)
        3. 最方便的是使用 `using namespace std;`，这样命名空间 std 内定义的所有标识符都有效 (就像被声明为全局变量一样，完整语句 A 改写为：`cout << hex << 5.0 << endl`)

* 若输入则采用 `cin` 输入
```c++
#include <iostream>
using namespace std;

int main()
{
    int age;
    cin >> age;
    cout << "Hello World! I'm "<< age << " today!" << endl;
}
```

## 字符串 | String

* 首先要加入库 `<string>`
* 定义字符串变量 —— `string str;`
* 初始化字符串变量 —— `string str = "Molan";`
* 输入输出字符串即使用 `cin`, `cout` —— `cin >> str; cout << str;`
* C++ 中的字符串变量支持类似整型变量的操作 —— `+` (拼接) ···

```c++ title="b.cpp"
#include <iostream>
using namespace std;

int main()
{
    int age;
    string name;
    cin >> age >> name;
    name += " (Enl_Z) "
    cout << "Hello World! " << name << " is " << age << " today!"<< endl;
}
```

```bash
$ g++ b.cpp; ./a.out
18 Molan
Hello World! Molan (Enl_Z) is 18 today!
```

* `string` 不需要像 `char str[10]` 一样设置长度，直接使用 `string str;` 即可 (内部会自动调整长度，且字符串末尾无 `\0`)
* `string` 变量支持赋值，即 `str1 = str2;` 是合法的

> 采用 `string str("Hello");` 和 `string str = "Hello";` 是一样的 (此种初始化方法对其他变量也适用)

### Pointers to Objects

> 正交: 若有某个操作对某个数据类型是可用的，则理论上应满足其对所有数据类型可用 (如，取地址对整数可用则应对 `string` 也可用)

* Operators with Pointers
    * `&` : get address (e.g. `ps = &s;` )
    * `*` : get the object (e.g. `(*ps).length()` )
    * `->` : call the function (e.g. `ps->length()` )
* Two Ways to Access Objects
    * `string s;`
        * `s` is the object itself
        * 此时，对象已经被创建并初始化为一个默认的值 (由类决定, 调用类的构造函数初始化)
    * `string* ps;`
        * `ps` is a pointer to an object
        * In this time, the value of `ps` is still unknown
* Assignment
    1. `string s1, s2;`
        * `s1 = s2;`
    2. `string *ps1, ps2;`
        * `ps1= ps2`

### Dynamic memory allocation

> `new` 和 `delete` 都是运算符, c++ 中虽然也有 `malloc`，但最好不要再使用

* `new`
    * `new int;` (类似于 `malloc(sizeof(int))` 申请一个 `int` 的空间)
    * `new Stash;` (`Stash` 是一个类，此处申请了一个 `Stash` 的空间，但不同 `malloc` 的是其还调用构造函数进行了初始化)
    * `new int[10]`
    
    > `new` is the way to allocate memory as a program runs. Pointers become the only access to that memory.
    > `new` 没有空间的时候不会返回 `NULL` 而是抛异常

* `delete` —— 调用析构函数, 在析构函数中用于释放类内部动态分配得到的资源  (由于内置类型没有析构函数，所以 `delete` 内置类型指针时，什么也不需要做)
    * `delete p;`
    * `delete[] p;`
    > `delete` enables you to return memory to the memory pool when you are finished with it.

### Dynamic Arrays

* `int * psome = new int[10];`
    * The `new` operator returns the address of the first element of the block.
* `delete [] psome;`
    * The presence of the brackets tells the program that it should free the whole array, not just the element (`delete` 无法指定数量，即方括号内无法填入数字)
  
??? example
    ```c++
    int *a = new int[10];
    a++; delete[] a;
    ```
    此时 `delete[] a;` 会出错，因为 `a++` 后在这张表中没有 `a` 这一项，而是有 `a-1`

### Tips for new & delete

* Don't use `delete` to free memory that `new` didn't allocate
* Don't use `delete` to free the same block of memory
* Use `delete []` if you used `new[]`
* Use `delete`(without brackets) if you used `new` to allocate a single entity
* It is safe to apply delete to the null pointer (nothing happens)

## Class

### reference

* Reference is a new way to manipulate objects in C++
    * 在 c 中 `char c; char &r = c;` //a reference to a character
    * `r` is regarded as a reference to a character `c`
* 若变量是本地或全局变量，在声明变量的时候，必须对其做绑定
* 如果是参数列表或成员变量，不需要给出绑定

#### Rules of references

* References must be initialized when defined
* As a function argument
    * `void f(int &x)`
    * `f(y);` //initialized when function is called 
* Bindings don't change at run time (即不可以解绑)
* The target of a reference must have a location (即引用的对象只能是左值)
    * `void func(int &);`
    * `func(i * 3);`    //warning or error!

#### Points vs. References

* References
    * can't be null
    * are dependent on an existing variable, they are an alias for an variable
    * can't change to a new "address" location
* Pointers
    * can be set to a null
    * pointer is independent of existing objects
    * can change to point to a different address
  
#### Restrictions

* No references to references (e.g. `int i; int &r = i; int &k = r;` ×)
* No pointers to references (e.g. `int&* p;` ×) (Allow reference to pointer —— `void f(int*& p);`)
* No arrays of references 

### Point | 点

=== "C 版本 struct"

    ```c++ 
    #include <iostream>
    using namespace std;

    typedef struct Point{
        float x;
        float y;
    } Point;

    void print(const Point *p)
    {
        cout << p->x << " , " << p->y << endl;
    }
    void move(Point *p, int dx, int dy)
    {
        p->x += dx;
        p->y += dy;
    }
    int main()
    {
        Point a, b;
        a.x = b.x = 1;
        a.y = b.y = 1;
        //也可以写作 
        //Point a = {1, 1}, b = {1, 1};
        move(&a, 2, 2);
        print(&a);
        print(&b);
    }
    ```
=== "C++ 版本"

    ```c++ 
    #include <iostream>
    using namespace std;

    struct Point{   
        float x;
        float y;
        void print()
        {
            cout << x << " , " << y << endl;
        }
    } ;

    void move(Point *p, int dx, int dy)
    {
        p->x += dx;
        p->y += dy;
    }
    int main()
    {
        Point a, b;
        a.x = b.x = 1;
        a.y = b.y = 1;
        move(&a, 2, 2);
        a.print();
        b.print();
    }
    ```
* 其中，无需使用 `typedef` 也可以直接声明 `Point a, b;`
* C++ 支持将函数也写入结构体中 (如 print 函数，只是此时不需要 const Point *p)
* 而对于 `move` 也具有另一种写法 (即不带 body 的函数) 

```c++
···
struct Point{   
        float x;
        float y;
        void init(int ix, int iy)
        {
            x = ix;
            y = iy;
        }
        void print()
        {
            cout << x << " , " << y << endl;
        }
        void move(int dx, int dy);
    } ;

    void Point::move(int dx, int dy)       //struct 中不带 body ，所以需要另给出 body
    {
        x += dx;
        y += dy;
    }

    int main()
    {
        Point a, b;
        a.init(1, 1);
        b.init(1, 1);
        a.move(2, 2);
        a.print();
        b.print();
    }
```

* 上述表示 C 中 struct 中支持成员变量，C++ 中不仅支持成员变量也支持成员函数 (这就是 C++ 的类)
* C++ 中 struct 和 class 基本是通用的，唯有几个细节不同

??? "struct vs. class"
    * 使用 class 时，类中的成员默认都是 private 属性的；而使用 struct 时，结构体中的成员默认都是 public 属性的
    * class 继承默认是 private 继承，而 struct 继承默认是 public 继承
    * class 可以使用模板，而 struct 不能
    
    ```c++
    class Point{
    public:
        void init(int x, int y);
        void move(int dx, int dy);
        void print() const;

    private:
        int x;
        int y;
    };
    ```
    > [知乎 - 参考](https://zhuanlan.zhihu.com/p/47808468)
    > [CSDN - 参考](https://blog.csdn.net/alidada_blog/article/details/83419757)

#### ::resolver

```c++
void S::f()
{
    ::f();  //Would be recursive otherwise
    ::a++;  // Select the global a
    a--;    //  The a at class scope
}
```

* < Class Name > :: < function name > (:: 是符号, not operator)
* :: < function name >
* `::f();` 在当前语境下，若不加 '::' 表示调用自己。加上 '::' 表示 f 不是自己，是 free 的函数
* 同理, `::a++;` 也表示全局变量 a; `a--;` 指成员变量 a
 
### Stash

!!! note
    Stash 是一种容器，可以保存任意数据类型的变量 (将任意数据类型的变量看作字节数组)

#### this

> 为什么成员函数不需要引入类似 `Point *p`, 也能识别是哪个变量

* Realized with `this` 
* `this` is a hidden parameter for all member functions, with the type of the struct

??? example
    `void Stash::init(int sz)`
    --> can be regarded as
    `void Stash::init(Stash *this, int sz)`

* To call the function, we must specify a variable

??? example
    `Stash a;`
    `a.init(10);`
    --> can be regarded as
    `Stash::init(&a, 10);`

* Inside member functions, you can use `this` as the pointer to the variable that calls the function
* `this` is a natural local variable of all structs member functions that <u>you can not define, but you can use it directly</u>

??? example "this 的一种用法"
    ```c++
    struct Stash{
        float x;
        float y;
        void init(int x, int y)
        {
            this->x = x;
            this->y = y;
        }
    }
    ```



