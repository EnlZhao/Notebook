!!! example
    ```makefile
    C_SRC       = $(sort $(wildcard *.c))
    OBJ		    = $(patsubst %.c,%.o,$(C_SRC))

    file = main.o
    all:$(OBJ)
        
    %.o:%.c
        ${GCC} ${CFLAG} -c $<
    clean:
        $(shell rm *.o 2>/dev/null)

    ```
!!! quote 
    [CSDN](https://blog.csdn.net/weixin_38391755/article/details/80380786)