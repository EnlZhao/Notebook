# Container | 容器

## STL

!!! abstract
    在 C++ 中，容器是 STL 中的模板提供的
 
* STL = Standard Template Library
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
    * A pair class (pairs of anything, int/int, int/char, etc)
    * Containers
        * vector (expandable array)
        * deque (expandable array, expands at both ends)
        * list (double-linked)
        * sets and maps
    * Basic Algorithms (sort, search, etc)
* All identifiers in library are in std namespace (`using namespace std;`)
* The three parts of STL
    * Containers
    * Algorithms
    * Iterators
* Top 3 data structures
    * map
        * Any key type, any value type
        * sorted
    * vector
        * like c array, but auto-extending
    * list
        * doubly-linked list
* All Sequential Containers
    * vector: variable array
    * deque: dual-end queue
    * list: double-linked-list
    * forward_list: as it
    * array: as "array"
    * string: char.array

### vector

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
    * `::iterator` 表示 vector 中的类 `iterator`，可以对 `vector of int` 枚举, 拿出来的每一个都应该是 `int`
    * `begin` 会返回一个枚举器，用这个枚举器可以枚举容器中的每一个元素

* It is able to increase its internal capacity as required: as more items are added, it simply makes enough room for them
* It keeps its own private count of how many items it is currently storing. Its size method returns the number of objects currently in it
* In maintains the order of items you insert into it. You can later retrieve them in the same order.

#### Basic Vector Operations

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
    * `V.insert(position, e);`
    * `V.erase(position);`
    * `V.clear();`
    * `V.find(first, last, item);`
