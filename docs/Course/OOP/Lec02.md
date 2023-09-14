---
date: 2023-03-03 14:00
---

# Step in Object-Oriented 

> Objects = Attributes + Services

* 首先将 struct 改为 class (struct 是指内部成员统统对外开放的, class 是默认外部不可访问的)

> 对外与对内相对应，对内指可以在 struct 中或者成员函数中使用

??? example
    ```c++
    ···
    class Point{   
        float x;
        float y;
    public:
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
            a.x = b.x = 1;  // --+
            a.y = b.y = 1;  // --+-- Error: 不可访问
            a.move(2, 2);
            a.print();
            b.print();
        }
    ```

## Constructor

* Guaranteed initialization with the constructor
    * If a class has a constructor, the compiler automatically calls that constructor at the point an object is created, before client programmers can get their hands on the object.
    * The name of the constructor is the same as the name of the class
    * `class` 中的构造函数，函数名和类的名字一致 (无返回类型)
* Constructors with arguments
    * The constructor can have arguments to allow you to specify how an object is created, give it initialization values, and so on.
    * 当同名成员函数存在参数时，用类构造对象的时候要主动给出相应的值, 如 `Point a(1, 1);`
    * `Point *p = new Point(5, 6);` ——> `new` 做了两件事
        1. 申请空间
        2. 调用 Point 的构造函数，把 5 和 6 传递给构造函数 (但构造函数执行的时候这个对象已经存在了，构造函数做的事情是初始化)
        > 构造函数不做内存分配

    ??? example
        ```c++
        ···
        class Point{
        private:
            float x;
            float y;
        public:
            Point(int x, int y);    //名字和类的名字一样，且无返回类型
            void print();
            void move(int dx, int dy);
        };

        Point::Point(int x, int y)
        {
            this->x = x;
            this->y = y;
        }
        void Point::print()
        {
            ···
        }
        void Point::move(int dx, int dy)
        {
            ···
        }
        int main()
        {
            Point a(1, 2), b(3, 4);
            ···
        }

        ···
        ```

* 函数的重载 —— 在 class 中有多个同名的成员函数 (但需要保证参数表不同)

    ??? example
        ```c++
        ···
        class Point{
        private:
            float x;
            float y;
        public:
            Point(int deep);
            Point(int x, int y);
            void print();
            void move(int dx, int dy);
        };
        Point::Point(int deep)
        {
            x = y = deep;
        }
        ···
        int main()
        {
            ···
            Point c(10); //会调用参数为 deep 的成员函数
            ···
        }
        ···
        ```
    
        * `Point c(10);` 等价于 `Point c=10;` (单个赋值都可以用圆括号或等号)
        * 由于存在构造函数，此时 (即使 float x 和 float y 都是 public) 不再支持 结构那样的方式初始化 (`Point a = {1, 1};`)
      
* The default constructor
    * A default constructor is one that can be called with <u>no arguments</u>
    * 指的是写了一个构造函数，这个构造函数没有参数
    * 如果未给出构造函数，编译器会给出一个什么都不做的构造函数来通过编译

    ??? example
        ```c++
        struct Y{
            float f;
            int i;
            Y(int a);
        }
        ```

        * 此时: 
            * `Y y1[] = {Y(1), Y(2), Y(3)};` √
            * `Y y2[2] = {Y(1)};` × (Y 有构造函数且不是默认构造函数, 如代码需要给出两个构造函数)
            * `Y y3[7];` × (同理，有默认构造函数才可以这么写)

## The destructor

* In C++, cleanuo is as important as initialization and is therefore guaranteed with the destructor
* The destructor is named after the name of the class with a leading tidle (~). The destructor never has any arguments.
    * The destructor is called automatically by the compiler when the objects goes out of scope.
    * The only evidence for a destructor call is the closing brace of the scope that surrounds the object.
    * 如下，析构函数 `~Y();` 会在对象的空间被回收之前被自动调用.

    ```c++
    class Y{
    public:
        ~Y();
    };
    ```

    ??? example
        ```c++
        ···
        class Point{
        private:
            float x;
            float y;
        public:
            Point(int deep);
            Point(int x, int y);
            Point(){x = 31, y = 17;}
            ~Point()
            {
                cout << "~";
                print();
            }
            void print();
            ···
        }
        ···
        int main()
        {
            Point a(1, 2), b(3, 4);
            Point *p = new Point(5, 6);
            Point c(10);
            Point d;
            d.print();
            delete p;
        }
        ```
        ```bash
        $ ./a.out
        31,17
        ~5,6    # 对应 p
        ~31,17  # 对应 d
        ~10,10  # 对应 c
        ~3,4    # 对应 b
        ~1,2    # 对应 a
        ```

        * 因为所有变量定义在 main 中，当发生到 `delete` 时本地变量生存期结束，即所有变量都要析构 (析构的顺序时构造的逆序)
        * 如果 main 中修改如下

        ```c++
        int main()
        {
            Point a(1, 2), b(3, 4);
            Point *p = new Point(5, 6);
            {
                Point c(10);
            }
            Point d;
            d.print();
            delete p;
        }
        ```
        ```bash
        $ ./a.out
        ~10,10  # 对应 c
        31,17
        ~5,6    # 对应 p
        ~31,17  # 对应 d
        ~3,4    # 对应 b
        ~1,2    # 对应 a
        ```

        * 因为 c 出了括号就结束了，所以先被析构

??? info "Global objects"
    * Consider

    ```c++
    #include "X.h"
    X global_x1(1, 2);
    X global_x2(3, 4);
    ```

    * Constructors are called before entering `main()`
        * Order controlled by appearance in file
        * In this case, `global_x1` before `global_x2`
        * `main()` is no longer the first function called
    * Destructors called when
        * `main()` exits
        * `exit()` is called

## Storage allocation

* The compiler allocates all the storage for a scope at the opening brace of that scope
* The constructor call doesn't happen until the sequence point where the object is defined
  
## Initialization

### Initializer list

!!! note "code"
    ```c++
    class Point{
    Private:
        const float x, y;
        Point(float xa = 0.0, float ya = 0.0): x(xa), y(ya){}
    };
    ```

    > `Point(float xa = 0.0, float ya = 0.0): x(xa), y(ya){}` 中 `: x(xa), y(ya)` 即初始化列表形式

* Can initialize any type of data
    * pseduo-constructor calls for built-in types
    * No need to perform assignment within body of constructor
* Order of initialization is order of **declaration**
    * Not the order in Initializer list!
    * Destoryed in reverse order of declaration
    * 比如即便在 Initializer list 中 `Point(float xa = 0.0, float ya = 0.0): y(ya), x(xa){}`， `ya` 在 `xa` 之前声明，但是由于成员变量声明 `x` 在 `y` 之前，所以 `x` 会先被初始化
    * `Point(float xa = 0.0, float ya = 0.0): y(ya), x(y){}` 就不会符合 `x = y = ya`

### Others

??? note "编程规范"
    * Declarations vs. Definitions
        * cpp file —— compile unit
        * Only declarations are allowed to be in .h (). Declarations are as follows: 
            * extern variables
            * function prototypes
            * class/struct declaration
            * inline function
            * Others are Definitions
    * Standard header file structure 
        * All .h files should look like this: 

        ```c++
        #ifdef  HEADER_FLAG
        #define HEADER_FLAG
        //Type declaration here
        #endif  //HEADER_FLAG
        ```

    * Tips for header
        * One class declaration per header file
        * Associated with one source file in the same prefix of file name
        * The contents of a header file is surrounded with `#ifdef #define #endif` 
