# Lecture 1 

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
        * `s` 本身就是对象
        * 此时，对象已经被创建并初始化为一个默认的值 (由类决定, 调用类的构造函数初始化)
    * `string* ps;`
        * `ps` 是指向对象的指针
        * 此时，`ps` 的值还是未知的
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
* `delete`
    * `delete p;`
    * `delete[] p;`




