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

