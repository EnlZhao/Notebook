---
date: 2023-04-03 12:00
---

# Container | 容器

## STL

!!! abstract
    在 C++ 中，容器是 STL 中的模板提供的
 
* STL = Standard Template Library | 标准模板库
* Part of the ISO Standard C++ Library
* Data Structures and algorithms for C++

??? success "Why use STL"
    * Reduce development time
    * Code readability
    * Robustness
    * Portable code
    * Maintainable code
    * Easy

* Library includes:
    * A **Pair** class (pairs of anything, int/int, int/char, etc)
    * Containers
        * **vector** (expandable array)
        * **deque** (expandable array, expands at both ends)
        * **list** (double-linked)
        * **sets** and **maps**
    * Basic Algorithms (sort, search, etc)
* All identifiers in library are in std namespace (`using namespace std;`)
* The three parts of STL
    * Containers
    * Algorithms
    * Iterators
* Top 3 data structures
    * `map`
        * Any key type, any value type
        * sorted
    * `vector`
        * like c array, but auto-extending
    * `list`
        * doubly-linked list
* All Sequential Containers
    * vector: variable array
    * deque: dual-end queue
    * list: double-linked-list
    * forward_list: as it
    * array: as "array"
    * string: char.array

## Vector Class

??? example
    ```c++
    #include <iostream>
    using namespace std;
    // Use namespace so that you can refer to vectors in C++ library
    #include <vector>

    int main()
    {
        vector<int> x;  //Just declare a vector of ints(no need to worry about size)
        for(int a = 0; a < 1000; a++)
        {
            x.push_back(a); //Add elements
        }
        /* Have a pre-defined iterator for vector class, can use it to print out the items in vector */
        vector<int>::iterator p;    
        for(p = x.begin(); p < x.end(); p++)
        {
            cout << *p << " ";
        }
        return 0;
    }
    ```

    * `vector<int> x;` 中 `x` 是变量的名字，`<int>` 表示要在 vector 里面放 `int`类型的数据
    * <u>`::iterator` 表示 vector 中的类 `iterator`，可以对 `vector of int` 枚举, 拿出来的每一个都应该是 `int`</u>
    * `begin` 会返回一个枚举器，用这个枚举器可以枚举容器中的每一个元素

* It is able to increase its internal capacity as required: as more items are added, it simply makes enough room for them
* It keeps its own private count of how many items it is currently storing. Its size method returns the number of objects currently in it
* In maintains the order of items you insert into it. You can later retrieve them in the same order.

### Basic Vector Operations

* Constructors 
    * `vector<ElementType> c;`
    * `vector<ElementType> c1(c2);  //c1 可以得到 c2 里的所有内容`
* Simple Methods
    * `V.size(); //num items`
    * `V.empty(); //Judge if empty`
    * `==, !=, <, >, <=, >= //比较两个 vector 的大小，依次拿对应元素比较`
    * `V.swap(v2); //swap 两个 vector 的全部内容`
* Iterators
    * `I.begin(); //first positiion`
    * `I.end();  //last position`
* Element access
    * `V.at(index)`
    * `V[index]`
    * `V.front(); //first item`
    * `V.back();  //last item`
* Add/Remove/Find
    * `V.push_back(e);`
    * `V.pop_back(e);`
    * `V.insert(position, e); // position 是一个 iterator，不能使用 1，2，3`
    * `V.erase(position); // size will change after "erase"`
    * `V.clear();`
    * `V.find(first, last, item);`

??? warning "Pitfalls"

    === "WRONG"
        * Accessing an invalid vector<> element
            * `vector<int> v;`
            * `v[100] = 1; //Whooops!`

    === "RIGHT"
        * use `push_back()` 
        * Preallocate with constructor
        * Reallocation with `reserve()`
        * Check `capacity()` 

## List Class

> 双向链表

* Same basic concepts as vector
    * Constructors
    * Ability to compare lists (==, !=, <, >, <=, >=)
    * Ability to access front and back of list
        * `x.front(), x.back()`
    * Ability to assign items to a list, remove items 
        * `x.push_back(item), x.push_front(item)`
        * `x.pop_back(), x.pop_front()`
        * `x.remove(item)`

??? example "code"
    ```c++ title="Sample List Application"
    #include <iostream>
    #include <list>
    #include <string>
    using namespace std;
    int main()
    {
        list<string> s;
        s.push_back("hello");
        s.push_back("world");
        s.push_front("tide");
        s.push_front("crimson");
        list<string>::iterator p;
        for(p = s.begin(); p != s.end(); p++)
        {
            cout << *p << " ";
        }
        cout << endl;
    }
    ```

    * Note the termination condition for the for loop: `p != s.end()`

??? warning "Pitfalls"
    <!--
    * Not using `empty()` on list<>
        * Slow `if(my_list.count() == 0) { }`
        * Fast `if(my_list.empty()) { }`
    -->

    === "WRONG"
        * Using invalid iterator
            * `list<int> L; list<int>::iterator li;`
            * `li = L.begin();  L.erase(li);`
            * `++li; // WRONG - 此时 li 已经被 erase`

    === "RIGHT"
        * Use return value of erase to advance
            * `li = L.erase(li); //RIGHT`
            * 此时 li 指向的是原来的下一个

## Maps

* Maps are collections that contain pairs of values.
* Pairs consist of a **key** and a **value** (故声明要指定两个类型)
* Lookup works by supplying a key, and retrieving a value
* An example: a telephone book

??? example
    ```c++
    #include <iostream>
    #include <string>
    #include <map>
    using namespace std;

    int main()
    {
        map<string, float> price;
        price["apple"] = 0.75;
    }
    ```

??? warning "Pitfalls"

    === "WRONG"
        * Inadvertently inserting into map<>
            * `if(foo["bob"] == 1)  //silently created entry "bob"`

    === "RIGHT"
        * Use `count()` to check for a key without creating a new entry
            * `if(foo.count("bob"))`

## Iterator

> use list as example `list<int> L;`

* Declaring
    * `list<int>::iterator li;`
* Front of container
    * `li = L.begin();`
* Past the end
    * `li = L.end();`
* Can increment
    * `li = L.begin();`
    * `++li; // second item`
* Can be dereferenced
    * `*li = 10;`

## Self-defined classes in STL Containers

* Might need:
    * Assignment Operator -> `operator=()`
    * Default Constructor
* For sorted types, like map<>
    * Need less-than operator -> `operator<()`
        * Some types have this by default (`int, char, string`)
        * Some do not (`char *`)

??? example
    ```c++
    ···
    class Student{
    public:
        int x;
        Student(int k) : x(k) {}
    };
    int main()
    {
        vector<Student>  ss;   
        vector<Student&> sl;   
        vector<Student*> sp;    
        ···
    }
    ```

    * `vector<Student*> sp;` 表示 vector 中存的是指针

## Other data structures

* set, multiset, multimap
* queue, priority_queue
* stack, deque
* slist, bitset, valarray

