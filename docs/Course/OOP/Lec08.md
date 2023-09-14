---
date: 2023-06-23 8:23
---

# Templates | 模板

??? question "Why templates"
    * Suppose you need a list of X and a list of Y
        * The lists would use similar code
        * They differ by the type stored in the list
    * Choices
        * Require common base class
            * May not be desirable
        * CLone code
            * preserves type-safety
            * hard to manage
        * Untyped lists
            * type unsafe

* Final choice: templates
    * Reuse source code
        * generic programming | 泛型编程
        * use types as parameters in class or function definitions
    * Function Template | 函数模板（制造函数）
        * Example: sort function
    * Class Template | 类模板(制造类)
        * Example: container such as stack, list, queue...
            * Stack operations are independent of the type of items in the stack
        * template member functions

## Function Templates

* Perform similar operations on different types of data
* Swap function for two int arguments:

``` c++
void swap(int& a, int& b) 
{
    int temp = a;
    a = b;
    b = temp;
}
```

* What if we want to swap floats, strings, Currency ...? (We need to rewrite the function for each type)
* But we can use a template!!!

???+ example "swap function template"
    ``` c++
    template <class T>  // 说明下面的东西是个模板
    void swap(T& a, T& b) 
    {
        T temp = a;
        a = b;
        b = temp;
    }
    ```

    * The <u>template</u> keyword introduces the template
    * The <u>class T</u> specifies a parameterized type name
        * class means any built-in type or user-defined type
    * Inside the template, use T as a type name

* Template Instantiation -- Generating a declaration from a template class/function and template arguments:
    * Types are substituted into template
    * New body of function or class definition is created 
        * syntax errors, type checking
    * Specialization - a version of template for a particular argument(s)

* Interactions
    * Only exact match on types is used
    * No conversion operations are applied
  
    ``` c++
    swap(int, int); // OK
    swap(double, double); // OK
    swap(int, double); // Error
    ```

    * Implicit conversions are ignored
    * Template functions and regular functions coexist

* Overloading rules
    * Check first for unique function match
    * Then check for unique function template
    * Then do overloading on functions

    ``` c++
    void f(float i, float k);
    template <class T> 
    void f(T i, T k);
    f(1.0, 2.0);    // 模板
    f(1, 2);        // 模板
    f(1.2, 0);      // 两个类型不同，转成 float 调用 f(float, float)
    ```

* Function Instantiation
    * The compiler deduces the template type from the actual arguments passed into the function
    * Can be explicit: For example, if the parameter is not in the function signature (older compilers won't allow this)

    ``` c++
    template <class T>
    void f(void) { ... }
    f<int>(); // type T is int    
    ```

    * 在函数后面加尖括号，尖括号中的类型表示 `T` 的类型


## Class Templates

* Classes parameterized by type
    * Abstract operations from the types being operated upon
    * Define potentially infinite set of classes
    * Another step towards reuse
* Typical use: container classes
    * `stack<int>` --- a stack that is parameterized over int
    * `list<Currency&>`

!!! tip "Important"
    * 如果将类模板中函数的声明和定义分开写，则除类前要加 `template`, 每一个函数定义也要加 `template`
    * ==<u>所有的函数都是 `ClassName<T>::funcName()` 的形式</u>==
    
    ???+ example
        ``` c++
        template <class T>
        class Vector {
        public:
            Vector(int);
            ~Vector();
            Vector(const Vector&);
            Vector& operator=(const Vector&);
            T& operator[](int);
        private:
            int size;
            T* data;
        };
        template <class T>
        Vector<T>::Vector(int s) : size(s)
        {
            data = new T[s];
        }
        template <class T>
        T& Vector<T>::operator[](int i) 
        {
            if (i < 0 || i >= size) {
                throw "Index out of range";
            }
            else
            {
                return data[i];
            }
        }
        ```

* Templates can use multiple types
  
    ```c++
    template <class Key, class Value>
    class HashTable 
    {
        const Value& lookup(const Key&) const;
        void install(const Key&, const Value&);
        ...
    };
    ```
    
* Templates nest --- they're just new types
    * `Vector<Vector<double *> >`

* Type arguments can be complicated
    * `Vector< int (*)(Vector<double>&, int) >` --- 一个 `Vector` 里面是函数指针，指针指向的函数的参数是 `Vector<double>&` 和 `int`，返回值是 `int`

* Expression parameters
    * Template arguments can be *constant* expressions
    * Non-Type parameters
        * can have a default argument

    ``` c++
    template <class T, int size = 100>
    class Vector 
    {
        ...
    private:
        T data[size];   // fixed size array
    };
    ```

    ???+ note "Usage:Non-type parameters"
        * Usage
            * `Vector<int, 100> v;`
            * `Vector<int, 50 * 2> v;`
            * `Vector<int> v;` --- uses default `size = 100`
        * Summary
            * Embedding sizes not necessarily a good idea
            * Can make code faster
            * Makes use more complicated --- size argument appears everywhere
            * Can lead to code bloat

!!! bug "Template programming"
    * 一个类模板的全部都应该在一个头文件中，而不是声明和定义分开放在两个文件中，否则编译器会链接失败
    * 大多数情况下，类模板的函数都做成 `inline`


???+ info "Templates and Inheritance"
    * Templates can inherit from non-template classes

    ``` c++
    class Derived : public Base
    {
        ...
    };
    ```

    * Templates can inherit from template classes | 当实例化 Derived 时，还需要同步实例化 Base

    ``` c++
    template <class T>
    class Derived : public Base<T>
    {
        ...
    };
    ```

    * Non-template classes can inherit from template classes

    ``` c++
    class Derived : public Base<int>
    {
        ...
    };
    ```