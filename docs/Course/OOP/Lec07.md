---
date: 2023-06-20 12:00
---

# Copy Ctor & Overloaded Operators | 拷贝构造与重载运算符

## Copy Ctor | 拷贝构造

??? example "一道题"
    === "题目"
        For the code below
        ``` c++
        void f()
        {
            Stash students();
            ···
        }
        ```
        which statement is RIGHT for the line in the function `f()`?
        1. This is a variable definition, while students is an object of Stash, initialized with the default constructor.
        2. This is a function prototype, while students is a function returns an object of Stash.
        3. This is a function call.
        4. This is illegal in C++.
    === "答案"
        1. false : 构造对象如果没有参数，不能加括号
        2. true : 函数原型声明是允许在函数内部发生的
        3. false
        4. false

* Copying 
    * Create a new object from an existing one | 在 C 中与传数组不同，函数的参数如果是结构体会在函数内部复制整个结构，而数组是指针 --- C++ 也是这样

    ``` c++
    // Currency as pass-by-value argument
    void func(Currency c)
    {
        // ...
    }
    ···
    Currency cur(10, 50);
    func(cur);  // cur is copied to c
    ```

    * 此时 func 中的 c 是 cur 的拷贝，在调用 `func` 的时候会调用拷贝构造函数

### The copy constructor

* Copying is implemented by the **copy constructor**
* Has the unique signature `ClassName::ClassName(const ClassName &)`
    * Call-by-reference is used for the explicit parameter
* C++ builds a copy ctor for you if you don't provide one
    * Copies each member variable --- Good for numbers, objects(会递归调用对象中的拷贝构造函数), arrays
    * Copies each pointer -- 源对象和拷贝构造对象指针相同，指向同一片内存区域
* 当不需要全盘拷贝 or 对象中有指针，需要自己写 Copy Ctor

!!! note "延申"
    === "code"
        ``` c++
        // Currency as pass-by-value argument
        Currency func(Currency c)
        {
            // ...
        }
        ···
        Currency cur(10, 50);
        Currency cur2 = func(cur);  // cur is copied to c
        ```
    === "explanation"
        * `Currency cur2 = func(cur);` 并未调用拷贝构造函数
        * 函数返回 int 时，返回值放在寄存器中；返回结构体时，返回值放在栈中。栈的空间是在 caller 的内存空间中
        * `cur2` 的赋值是在 callee 中完成的

* When are Copy Ctor called
    * During call by value

    ``` c++
    void func(Currency c)
    {
        // ...
    }
    ···
    Currency cur(10, 50);
    func(cur);  // cur is copied to c
    ```

    * During initialization

    ``` c++
    Currency cur(10, 50);
    Currency cur2 = cur;    // cur is copied to cur2
    Currency cur3(cur);     // cur is copied to cur3
    ```

    * During function return

    ``` c++
    Currency func()
    {
        Currency cur(10, 50);
        return cur;     // cur is copied to the return value
    }
    ···
    Currency cur2 = func(); // cur is copied to cur2
    ```

* Constructions vs. Assignment
    * <u>Every object is constructed once</u> -> 赋值的时候不发生拷贝构造
    * Every object should be destroyed once
        * Failure to invoke delete()
        * Invoking delete() more than once
    * Once an object is constructed, it can be the target of many assignment operations
    * 赋值、构造均为 member-wise, 即按照成员变量的顺序进行赋值、构造（bit-wise 是按照内存中的顺序进行全部赋值、构造）

## Overloaded Operators | 重载运算符

* Allows user-defined types to act like built in types
* Another way to make a fucntion call

??? note 
    > unary and binary operators can be overloaded

    * `+  -  *  /  %  ^  &  |  ~`
    * `=  <  >  +=  -=  *=  /=  %=  ^=  &=  |=`
    * `<<  >>  >>=  <<=  ==  !=  <=  >=  &&  ||  !  ++  --`
    * `,  ->*  ->  ()  []`
    * `new  new[]  delete  delete[]`

    > operators that cannot be overloaded

    * `.  .*  ::  ?:`
    * `sizeof  typeid`
    * `static_cast  dynamic_cast  const_cast  reinterpret_cast`

* Restrictions
    * Only existing operators can be overloaded (you can't create a ** operator for exponentiation)
    * Operators must be overloaded on a class or enumeration type
    * Overloaded operators must
        * Preserve number of operands
        * Preserve precedence

### C++ overloaded 

* Just a function with an operator name ( Use the opertaor keyword as a prefix to name operator *(···) ) 
* Can be a member function 
    * Implicit first argument `const String String::operator +(const String &that);`
    * `string a, b; a + b;` -> be like `a.operator+(b);`
* Can be a global function
    * Both arguments explicit `const String operator +(const String &s1, const String &s2);`
* 加 `const` 是为了防止 `a + b = c` 这种情况发生

#### For Member functions

* Implicit first argument
* Developer must have access to the class definition
* Members have full access to the all data in the class
* No type conversion performed on receiver

``` c++
class Integer
{
public:
    Integer(int n = 0):i(n) {}
    const Integer operator +(const Integer &that) const
    {
        return Integer(i + that.i);
    }
private:
    int i;
};
Integer x(1), y(5), z;
z = x + y;  // x.operator+(y)
z = x + 3;  // 此时会把 3 构造成一个 Integer 对象
z = 3 + y;  // 此时不会把 3 变成 Integer 对象，但会尝试把 y 变成 int
```

* For binary operators(+, -, *, etc) member functions require one argument
* For unary operators(++, --, -, !, etc) member functions require no arguments
    * `const Interger Interger::operator-() const{ return Integer(-i); }`
    * `z = -x`

#### For global function

```c++
const Integer operator+ (const Integer& rhs, const Integer& lhs);
Integer x, y;
x + y; // -> operator+ (x, y)
```

* Explicit first argument
* Developer dose not need special access to classes
* May need to be a friend
* Type conversions performed on both arguments

!!! note "conversions"
    === "code"
        ``` c++
        z = x + y;
        z = x + 3;
        z = 3 + y;
        z = 3 + 4;
        ```
    === "explanation"
        * 前三个左右两个变量都会尝试构造成 `Integer`
        * 最后一个先进行 `3 + 4`, 随后把结果尝试构造成 `Integer`

* Global operators
    * binary operators requires two arguments
    * unary operators require one
    * If you don't have access to private data members, then the global function must use the public interface or use `friend`

    ``` c++ 
    class Integer
    {
        friend const Integer operator+ (const Integer& rhs, const Integer& lhs);
        ···
    };
    const Integer operator+ (const Integer& rhs, const Integer& lhs)
    {
        return Integer(lhs.i + rhs.i);
    }
    ```

???+ tip "Members vs. Free Function"
    * Unary operators should be members
    * `= () [] -> ->*` must be members
    * assignment operators should be members
    * All other binary operators as non-members

#### Argument Passing & Return Values

* Argument Passing
    * If it is read-only, pass it in as a const reference (except for built-in types)
    * make member functions const that do not modify the class (boolean operators, +, -, etc)
    * for global functions, if the left-hand side changes, pass as a reference (assignment operators)
* Return Values
    * Select the return type depending on the expected meaning of the operator. For example, 
        * For operator+, you need to generate a new object. Return as a const object so the result cannot be modified as an left-value.
        * Logical operators should return bool(or int for older compilers)

??? tip
    * Pass in an object it you want to store it
    * Pass in a reference or pointer if you want to do something to it
    * Pass in a const reference or pointer if you want to get the values
    * Pass out an object if you create it in the function
    * Pass out a reference or pointer of the passed in only
    * Never new something and return its pointer

#### The prototypes of operators

* `+ - * / % ^ & | ~`
    * `const Integer operator+ (const Integer& rhs, const Integer& lhs);`
* `! && || < > <= >= == !=`
    * `bool operator< (const Integer& rhs, const Integer& lhs) const;`
* `[]`
    * Must be a member function
    * Single argument
    * Implies that the object it is being called for acts like an array, so it should return a reference
        * `Integer v[10]; v[0] = 1;`
        * if you return pointer -> you should use `*v[0] = 1;`
* `++ --`
    * How to distinguish between prefix and postfix?
        * Prefix: `const Integer& Integer::operator++();`
        * Postfix: `const Integer Integer::operator++(int);`
    * postfix forms take an int argument -- compiler will pass in 0 as that int
    * User-defined prefix is more efficient than postfix

    ``` c++
    class Integer
    {
    public:
        const Integer& operator++()    // prefix
        {
            *this += 1;     // increment
            return *this;   // fetch
        }
        // int argument not used so leave it unnamed
        // won't get compiler warning
        const Integer operator++(int) // postfix
        {
            Integer old = *this;    // fetch
            ++(*this);              // increment
            return old;             // return old value
        }
        ···
        Integer x(1);
        ++x;    // calls x.operator++()
        x++;    // calls x.operator++(0)
    };
    ```

#### Stream

* Defining a stream extractor
    * Has to be a 2-argument <u>global(free) function</u>
    * First argument is an `istream&`
    * Second argument is a reference to a value

    ``` c++
    istream& operator>> (istream& in, T& obj)
    {
        // specfic code to read obj 
        ···
        return in;
    }
    ```

    * Return an `istream&` for chaining
    
    ``` c++
    cin >> a >> b >> c;
    ((cin >> a) >> b) >> c;
    ```

* Creating a stream inserter
    * First argument is an `ostream&`
    * Second argument is any value

    ``` c++
    ostream& operator<< (ostream& out, const T& obj)
    {
        // specfic code to write obj 
        ···
        return out;
    }
    ```

    * Return an `ostream&` for chaining

    ``` c++
    cout << a << b << c;
    ((cout << a) << b) << c;
    ```

* Creating manipulators
    * You can define your own manipulators

    ``` c++
    // skeleton for an output stream manipulator
    ostream& manipulator(ostream& out)
    {
        // specific code to manipulate out
        ···
        return out;
    }
    ostream& tab(ostream& out)
    {
        return out << '\t';
    }
    cout << "Hello" << tab << "World" << endl;
    ```

* Copying vs. Initialization

=== "code"
    ``` c++
    #include <iostream>
    using namespace std;
    class Fi
    {
    public:
        Fi() { cout << "Fi()" << endl; }
    };
    class Fee
    {
        int i;
    public:
        Fee(int) { cout << "Fee(int)" << endl; }
        Fee(const Fi&) { cout << "Fee(Fi)" << endl; }
        Fee& operator=(const Fee& that)
        {
            i = that.i;
            cout << "=()\n";
            return *this;
        }
    };
    int main()
    {
        Fee fee = 1;    // Fee(int)
        Fi fi;
        Fee fum = fi;   // Fee(Fi)
        fum = fi;
    }
    ```

=== "Output"
    ``` shell
    Fee(int)
    Fi()
    Fee(Fi)
    Fee(Fi)
    =()
    ```

=== "More"
    * 这种 `=` 并不安全，因为很可能发生 `fum = fum;` 的现象
    * 可改写为

    ``` c++
    T& T::operator=(const T& that)
    {
        // check for self assignment
        if(this != &that)
        {
            // perform assignment
            ···
        }
        return *this;
    }
    ```

* Assignment Operator
    * For classes with dynamically allocated memory declare an assignment operator(and a copy constructor)
    * To prevent assignment, explicitly declare `operator=` as `private`

### Value classes

!!! note
    * Appear to be primitive data types
    * Passed to and returned from functions
    * Have overloaded operators(often)
    * Can be converted to and from others types
    * like: Complex, Date, String

* User-defined Type conversions
    * A conversion operator can be used to convert <u>an object of one class</u> into <u>an object of another class</u> or <u>a built-in type</u>
    * Compilers perform implicit conversions using:
        * Single-argument constructors

        ``` c++
        class PathName
        {
            string name;
        public:
            //or could be multi-argument with defaults
            PathName(const string&);
            ~PathName();
        };
        ···
        string abc("abc");
        PathName xyz(abc);  //OK
        ```

        * implicit type conversion operators (Preventing implicit conversions)

            === "code"

                ``` c++
                class PathName
                {
                    string name;
                public:
                    explicit PathName(const string&);
                    ~ PathName();
                };
                ···
                string abc("abc");
                PathName xyz(abc);  // OK
                xyz = abc;  // error!
                ```

            === "explanation"
                * New keyword: <u>`explicit`</u>
                * 用在上述类似的函数前，表示此类构造函数函数只用于构造不用于类型转换

* 更通用/直接的类型转换方法 --- Operator conversion
    * Function will be called automatically
    * Return type is same as function name

    ``` c++
    class Rational
    {
    public:
        ···
        operator double() const;    // Rational to double (double() 可以是其他任何类型的名字)
    }
    ···
    Rational::operator double() const
    {
        return numerator_/(double)denominator_;
    }
    Rational r(1, 3);
    double d = 1.3 * r; // r => double
    ```

    !!! note "General form of conversion ops"
        * X::operator T()
            * Operator name is any type descriptor
            * No explicit arguments
            * No return type
            * Complier will use it as a type conversion from `X` to `T`

* C++ type conversions
    * Built-in conversions
        * Primitive 
            * `char -> short -> int -> float -> double (int -> long)`
        * Implicit (for any type T)
            * `T -> T&; T& -> T;  T* -> void*`
            * `T[] -> T*; T* -> T[]; T -> const T`
    * User-defined `T -> C`
        * if `C(T)` is a valid constructor call for `C`
        * if `operator C()` is defined for `T`

    * But it's better to avoid User-defined conversions. Use explicit conversion functions instead. For example:
    * In `class Rational` instead of the conversion operator, declare a member function `double to_double() const;`

* Overloading and type conversion
    * C++ checks each argument for a "best match"
    * Best match means cheapest
        1. Exact match is cost-free
        2. Matches involving built-in conversions
        3. User-defined type conversions

??? info "延申 - LValue vs. RValue"
    * 可以简单认为能出现在赋值号左边的都是左值：变量本身、引用；`*, []`运算的结果
    * 只能出现在赋值号右边的都是右值：字面量；表达式
    * 引用只能接受左值 -> 引用是左值的别名
    * 调用函数时的传参相当于参数变量在调用时的初始化
    
    !!! note "右值引用"
        * `int x = 20;` 左值
        * `int&& rx = x * 2;` x*2 的结果是一个右值，rx 延长其生命周期；rx 是右值引用（对右值的引用）-> 相当于把右值先固定下来
        * `int y = rx + 2;` 因此你可以重用它：42
        * `rx = 100; ` 一旦你初始化一个右值引用变量，该变量就成为了一个左值，可以被赋值
        * `int&& rrx1 = x;` ERROR：右值引用无法被左值初始化
        * `const int&& rrx2 = x` ERROR: 右值引用无法被左值初始化

    !!! note "右值引用的用途"
        ``` c++
        // 接收左值 
        void func(int& lref)
        {
            cout << "lvalue ref" << endl;
        }
        // 接收右值 -- 为了节省内存，右值引用可以接收右值，而不是拷贝一份
        void func(int&& rref)
        {
            cout << "rvalue ref" << endl;
        }
        int main()
        {
            int x = 10;
            func(x);    // lvalue ref
            func(10);   // rvalue ref
            return 0;
        }
        ```
        
        * 如果是左值引用，也要先放到一个变量中才能传递
        * 而右值引用不需要有，可以加速运算，减少内存拷贝