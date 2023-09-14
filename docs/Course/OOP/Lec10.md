---
date: 2023-06-23 14:54
---

# Smart Pointers | 智能指针

!!! abstract
    * `Templates`, `Inheritance`, `Reference Counting` 合起来实现 `Smart Pointers`
    * `Reference Counting` 是有多少个指针指向这个对象，如果没有指针指向这个对象，就 `delete` 这个对象

    ??? quote "Smart Pointer 的来源"
        *[C++ Strategies and Tactics, Robert B. Murray, 1993](https://dl.acm.org/doi/10.5555/134460)*


!!! success "Goals"
    * Introduce the code for maintaining **reference counts**
        * A reference count is a count of the number of times an object is shared
        * Pointer manipulations have to maintain the count
    * Class **UCObject**(Use-counted object) holds the count
    * **UCPointer** is a *smart pointer* to a UCObject
        * A smart pointer is an object defined by a class
        * Implemented using a template
        * Overloads operator->  and  unary operator*

## Reference counting

* Each shared object has a counter
* Initial value is 0
* Whenever a pointer is assigned `p = q`
    * Have to do the following

    ``` c++
    p->decrement(); // p's count will decrease 
    p = q;
    q->increment(); // q's count will increase
    ```

!!! note "StringRep"
    ``` c++
    #include "UCObject.hpp"
    #include <cstring>
    class StringRep:public UCObject
    {
    public:
        StringRep(const char *s)
        {
            if(s)
            {
                int len = strlen(s) + 1;
                m_pChars = new char(len);
                strcpy(m_pChars, s);
            }
            else
            {
                m_pChars = new char[1];
                *m_pChars = '\0';
            }
        }
        ~StringRep()
        {
            delete[] m_pChars;  // 引用计数是父类要做的事情
        }
        StringRep(const StringRep &sr)
        {
            int len sr.length();
            m_pChars = new char[len + 1];
            strcpy(m_pChars, sr.m_pChars);
        }
        int length() const
        {
            return strlen(m_pChars);
        }
        int equal(const StringRep &sp) const
        {
            return (strcmp(m_pChars, sp.m_pChars) == 0);
        }
    private:
        char *m_pChars;
        // reference semantics -- no assignment op!
        void operator=(const StringRep &){} // 不允许直接赋值，因也没有赋值的必要
    };
    ```

!!! note "String"
    ``` c++
    #include "UCPointer.hpp"
    #include "StringRep.hpp"
    class String
    {
    public:
        String(const char *s) : m_rep(0)
        {
            m_rep = new StringRep(s);
        }
        ~String(){}
        String(const String &s) : m_rep(s.m_rep) {}
        String &operator=(const String &s)
        {
            m_rep = s.m_rep;    // let smart pointer do work!
            return *this;
        }
        int operator==(const String &s) const
        {
            // overload -> forwards to StringRep
            return m_rep->equal(*(s.m_rep));    // smart ptr *
        }
        String operator+(const String &s) const;
        int length() const
        {
            return m_rep->length();
        }
        operator const char *() const;
    private:
        UCPointer<StringRep> m_rep; // m_rep 表面是是一个对象，语义上是一个指针
    };
    ```

    * `m_rep = new StringRep(s);` 中 `m_rep` 的类型是 `UCPointer`, `new` 的类型是 `StringRep *` 不能直接赋值，会调用 `UCPointer` 中的构造函数把 `StringRep *` 转换成 `UCPointer`

    ``` c++
    UCPointer(T *r = 0) : m_pObj(r)
    {
        increment();
    }
    ```

    ??? question "上述过程中的 reference count"
        === "question"
            * 在 `m_rep = new StringRep(s);` 赋值发生前 `reference count` 就已经 +1，整个赋值完成后 `reference count = 2` 
            * 这和我们的预期不符，我们希望 `reference count = 1`

        === "answer"
            * 其实在 `m_rep = new StringRep(s);` 因为类型的不同需要使用临时对象构造 `UCPointer` 再赋值给 `m_rep`
            * 所以在赋值完成后会把这个临时对象析构，`reference count -= 1 -> reference count = 1` 


[Critique]:
* `UCPointer` maintains reference counts
* `UCObject` hides the details of the count String is very clean
* `StringRep` deals only with string storage and manipulation
* `UCObject` and `UCPointer` are reusable
* Objects with cycles of `UCPointer` will never be deleted

??? info"Other smart pointers"
    * Standard library holder for raw pointers on stack
    * Releases resource when destroyed (latest)

    ``` c++
    template <class X> std::auto_ptr
    {
    public:
        explicit auto_ptr(X* = 0) throw();
        auto_ptr(auto_ptr&) throw();
        auto_ptr& operator=(auto_ptr&) throw();
        ~auto_ptr();
        X& operator*() const throw();
        X* operator->() const throw();
        ···
    };
    ```