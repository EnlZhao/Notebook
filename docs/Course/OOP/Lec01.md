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

