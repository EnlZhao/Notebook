# Introduction

[TOC]

---

> Introduction基本是系统Ⅱ中整个操作系统部分课上要讲的内容

### Interrupts and Traps 

* Interrupt transfers control to the interrupt service routine 
* **interrupt vector**: a table containing addresses of all the service routines
  
* incoming interrupts are disabled while serving another interrupt to prevent a lost interrupt
  
* **interrupt handler** must save the (interrupted) execution states


* A trap is a ==software-generated== interrupt, caused either by an error or a user request

  > error->比如除法指令被除数是0，user request->用户显式产生的trap比如系统调用，svc指令等

  * an **interrupt** is asynchronous; a **trap** is synchronous

  * e.g., **system call**, divided-by-zero exception, general protection exception...

* Operating systems are usually ==interrupt-driven==(有定时器中断，相应I/O中断等等)

  > 用户态的程序不允许直接操控磁盘控制器，但又需要读取其中的文件，会通过运行在特权态的操作系统内核操作（系统调用）

### Interrupt Handling 

* Operating system preserves the execution state of the CPU

  * save registers and the program counter (PC)

    > 保存上下文——寄存器和PC（保存到内存）

* OS determines which device caused the interrupt

  1. **polling** 

     > polling方式的中断，不论什么类型中断都会均为**跳转到一个统一的入口**，然后由软件去查询寄存器从而知道中断的来源

  2. **vectored** interrupt system

     > 硬件已经固定好（区分好中断类型，**不需要软件再去查询**），会**直接跳转到对应地址**

* OS handles the interrupt by calling the **device’s driver（设备驱动程序）**

  > 宏内核的重要组件。而对于微内核，往往设备驱动程序放在操作系统内核范围外，为了安全性，常将设备驱动程序的大部分代码移到用户态。

* OS restores the CPU execution to the saved state

### Interrupt-drive I/O Cycle

> to be continued

![image-20221208031159242](https://gitee.com/enl-z/typora_-images/raw/master/202212080311349.png)

* `device driver initiates I/O`是通过`MMIO`|`Memory Map I/O`的方式，实际是通过`STORE`指令去操作外设的中断控制器的地址；
  * 因为initiates I/O，写磁盘是很慢的过程，CPU不会一直等到I/O请求完成，当磁盘写完后会有图中`4`以Interrupt的形式告诉CPU（中断控制器硬连线的方式）

### I/O: from System Call to Devices, and Back 

* A program uses a **system call** to access system resources
  * e.g., files, network
* Operating system converts it to ==device access== and ==issues I/O requests==

  * I/O requests are sent to the device driver, then to the controller
  * e.g., read disk blocks, send/receive packets...

* OS puts the program to wait (==synchronous I/O==) or returns to it without waiting (==asynchronous I/O==)
  * OS may switches to another program when the requester is waiting

    > 即使是同步I/O, CPU也不是盲目等待状态。某一进程阻塞时，CPU可以调度另一进程

* I/O completes and the controller interrupts the OS

* OS processes the I/O, and then wakes up the program (synchronous I/O) or send its a signal (asynchronous I/O)

  > 一种自上而下，一种自下而上

### Direct Memory Access | DMA 

* DMA is used for high-speed I/O devices able to transmit information at close to memory speeds 
  * e.g., Ethernet, hard disk, cd rom...

* Device driver sends an I/O descriptor the controller
  * **I/O descriptor**: operation type (e.g., send/receive), memory address...

* <u>The controller transfers blocks of data between its *local buffer* and *main memory* **without CPU intervention**</u>(提高效率)
  
  > CPU会告诉显卡需要的数据起始地址在哪，有多长，随后由DMA搬运数据。搬运结束会通过硬中断的方式告诉CPU
  
  * only one interrupt is generated when whole I/O request completes

>  磁盘控制器分为常见的HDD和SSD

### Storage Structure 

* Main memory: the only large storage that CPU can directly access
  * **random access**, and typically **volatile**

* <u>Secondary storage: large **nonvolatile** storage capacity</u>
* Magnetic disks are most common second-storage devices (HDD)（系统Ⅲ）
    * rigid metal or glass platters covered with magnetic recording material 
  
* disk surface is logically divided into **tracks** and **sectors**
  
* disk controller determines the interaction between OS and the device

### Storage Hierarchy

* Storage systems can be organized in hierarchy
  * speed
  * cost
  * volatility

![image-20221208123411382](https://gitee.com/enl-z/typora_-images/raw/master/202212081234500.png)

* **Caching**: copying information into faster storage system
  * main memory can be viewed as a cache for secondary storage
  * CPU has a cache for main memory

#### Performance of Storages

|           Level           |                    1                    |               2               |        3         |        4         |
| :-----------------------: | :-------------------------------------: | :---------------------------: | :--------------: | :--------------: |
|           Name            |                register                 |             cache             |   main memory    |   disk storage   |
|       Typical size        |                 < 1 KB                  |            > 16 MB            |     > 16 GB      |     > 100 GB     |
| Implementation technology | custom memory with multiple ports, CMOS | on-chip or off-chip CMOS SRAM |    CMOS DRAM     |  magnetic disk   |
|      Access time(ns)      |                0.25-0.5                 |            0.5-25             |      80-250      |    5,000.000     |
|     Bandwidth(MB/sec)     |             20,000-100,000              |          5000-10,000          |    1000-5000     |      20-150      |
|        Managed by         |                compiler                 |           hardware            | operating system | operating system |
|         Backed by         |                  cache                  |          main memory          |       disk       |    CD or tape    |

### Caching

* Caching is an important principle, performed at many levels
  * e.g., in hardware, operating system, user program...
* **Caching**: data in use copied from slower to faster storage temporarily
* faster storage (cache) is checked first to determine if data is there

  * if it is, data is used directly from the cache (fast)

  * if not, data is first copied to cache and used there
* Cache is usually smaller than storage being cached
* Cache management is an important design problem
  * e.g., cache size and replacement policy

## MUltiprocessor Systems

* Most old systems have one single general-purpose processor

  * e.g., smartphone, PC, server, mainframe

  * most systems also have special-purpose processors as well

* Multiprocessor systems have grown in use and importance

  * also known as parallel systems, tightly-coupled systems
  * advantages: increased throughput, economy of scale, increased reliability -- graceful degradation or fault tolerance

  * two types: ==asymmetric multiprocessing== and ==symmetric multiprocessing (SMP)==

### Symmetric Multiprocessing Architecture 

> 各CPU有同等地位

![image-20221229091502728](https://gitee.com/enl-z/typora_-images/raw/master/202212290915782.png)

### NUMA 

* Non-Uniform Memory Access System
  * Access local memory is fast, scale well

> <u>每个CPU有自己的memory，但所有的memory是统一编制的，即CPU可以访问所有memory</u>

![image-20221229091612517](https://gitee.com/enl-z/typora_-images/raw/master/202212290916554.png)

### Clustered Systems

* Multiple systems work together <u>through high-speed network</u>
  * usually sharing storage via a storage-area network (SAN)

* Clusters provide a high-availability service that can survive failures
  * asymmetric clustering has one machine in hot-standby mode
  * symmetric clustering has multiple nodes running applications, monitoring each other

* Some clusters are designed for high-performance computing (HPC)
  * applications must be written to use parallelization

![image-20221229091816153](https://gitee.com/enl-z/typora_-images/raw/master/202212290918214.png)

### Distributed Systems

* A collection of separate, possibly heterogeneous, systems inter-connected through networks

* **Network OS** allows systems to exchange messages

* A **distributed system** creates the illusion of a single system

### Special-Purpose Systems

* Real-time embedded systems most prevalent form of computers
  * vary considerably
  * use special purpose (limited purpose) real-time OS

> 软实时：不严格在固定时间完成，硬实时（中断处理程序无嵌套）：严格按照要求在固定时间完成（不多不少）

* Multimedia systems
  * streams of data must be delivered according to time restrictions

* Handheld systems

  * e.g., PDAs, smart phones

  * limited CPU (?), memory(?), and power

  * used to use reduced feature OS (?)

### Dual-mode operation**

* Operating system is usually interrupt-driven 
  * Efficiency, regain control (timer interrupt)

* **<u>Dual-mode operation</u>** allows OS to protect itself and other system components
* **user mode** and **kernel mode** (or **other names**)
  
* a **mode** bit distinguishes when CPU is running user code or kernel code
  
* some instructions designated as **<u>privileged</u>**, only executable in kernel
  
* **<u>system call</u>** changes mode to kernel, return from call resets it to user

> 1. 分为两个模式是为了隔离，防止用户态程序去干扰操作系统内核的数据或数据结构。
>
> 2. 常用MMU部件（Memory Management Unit | 内存管理单元）来指定当CPU运行在特权态时可以访问所有物理地址空间，在用户态下只能访问有限空间达到二者的隔离
> 3. 部分指令必须在特权态下运行，比如关闭中断，打开中断、配置MMU的指令

### Transition between Modes 

* **System calls**, **exception**, **interrupts** cause transitions between kernel/user modes

![image-20221211040343687](https://gitee.com/enl-z/typora_-images/raw/master/202212110403765.png)

### Timer 

* Timer used to <u>prevent infinite loop or process hogging resources</u>

  * to enable a timer, set the hardware to interrupt after some period 

  * OS sets up a timer before scheduling process to regain control

    * the timer for scheduling is usually periodical(e.g., 250HZ)

    * **tickless kernel**: on-demand timer interrupts([Linux](https://lwn.net/Articles/549580/))


---

> <u>进程是资源分配的最小单元，线程是调度的最小单元</u>

### Process | 进程

> Process is the unit of resource allocation

#### Resource Management: Process Management 

* A *process* is a ==program in execution==

  * program is a ==passive== entity, *process* is an ==active== entity

  * a system has many processes running concurrently


> 不同进程之间是隔离的，即使是同一个program加载的进程

* Process needs resources to accomplish its task

  * OS reclaims all reusable resources upon process termination

  * e.g., CPU, memory, I/O, files, initialization data

* <u>进程是资源分配的最小单元，线程是调度的最小单元</u>


> 操作系统内核会管理分配给每一个内核的CPU资源、memory资源、I/O资源……是通过分时复用的方式，时间片轮转，每一个process运行一段时间就开始根据优先级调度

#### Process Management Activities

* Process creation and termination | 创建和中止

* Processes suspension and resumption | 暂停和恢复
* Process synchronization primitives | 同步

* Process communication primitives | 通信

* Deadlock handling | 死锁


> 在硬件层面，不同的`cpu core`上有不同的`register set | 寄存器集合`；
>
> 同时，不同`cpu core`上中断也是单独的，即每个core都可以响应任何权限内的中断。

<div align="center">
    <font color="red"; size=4px>
        考 试 & 考 研 重 点：进 程 状 态 的 切 换
    </font>
    <br>
    <font color="orange"; size=2px>
        详细状态切换后议
    </font>
</div>

![image-20221211065826923](https://gitee.com/enl-z/typora_-images/raw/master/202212110658983.png)

### Thread | 线程

#### From Process to Thread 

* Single-threaded process has one program counter 

  * **program counter** specifies location of next instruction to execute

  * processor executes instructions sequentially, one at a time, until completion

> 线程之间是不隔离的

* Multi-threaded process has **one program counter per thread**

* Quiz: What are the benefits of using thread instead of process?


> 不同的进程间要共享数据，如果是线程间共享，那数据会很庞大；
>
> 引入线程，线程可以被调度，只需要load/store再实现同步就可以实现共享。

* <u>一个进程中的多个线程共享了memory、global data、heap；不共享stack</u>
  * <u>每个线程有自己的栈和PC</u>
  * <u>线程和线程的栈不是隔离的，是可以直接访问到</u>

### Resource Management: Memory Management | 内存管理

* Memory is the main storage directly accessible to CPU 

  * data needs to be kept in memory before and after processing

  * all instructions should be in memory in order to execute

* Memory management determines what is in memory to **optimize CPU utilization** and **response time**, **provides a virtual view of memory for programmer**

* Memory management activities:

  * keeping track of which parts of memory are being used and by whom

  * deciding which processes and data to move into and out of memory

  * allocating and deallocating memory space as needed


> 管理CPU，管理Memory，做好同步占去操作系统内核的大部分工作

### Resource Management: File Systems | 文件系统

> * 介绍较少,系统Ⅲ
>
> * 将平时所使用的可视化的文件路径映射到物理存储介质上

* OS provides a uniform, logical view of data storage

  * **file** is a logical storage unit that abstracts physical properties

    * files are usually organized into **directories**(目录)

    * **access control** determines who can access the file

* File system management activities:

  * creating and deleting files and directories

  * primitives to manipulate files and directories

  * mapping files onto secondary storage

  * backup files onto stable (non-volatile) storage media

### Resource Management: I/O System Management

> 帮助用户态程序和外设打交道

* I/O subsystem hides peculiarities of hardware devices from the user

* I/O subsystem is responsible for:

  * manage I/O memory

    * **buffering**: to store data temporarily while it is being transferred

    * **caching**: to store parts of data in faster storage for performance

    * **spooling**: the overlapping of output of one job with input of other jobs

* OS May provide general **device-driver** interfaces(每一类设备都有对应的设备驱动程序)

  * good for programmers: object-oriented design pattern

  * bad from the security perspective: function pointers are heavily used

![image-20221220231706811](https://gitee.com/enl-z/typora_-images/raw/master/202212202317884.png)

### Separate Policy and Mechanism 

* Mechanism(机制): **how** question about a system | 怎么实现
  * How does an operating system performs a context switch

> 不同的调度器实现不同的Policy

* Policy(策略): **which** question 
  * Which process should the process to be switched

* Any other examples about mechanism & policy?

* Advantages & Disadvantages
  * Advantages of separation:
    * 增加整个的灵活性.

### Virtualization

* **Abstract** the hardware of a single computer (CPU/Memory/IO ...) into different environments

![image-20221221104000986](https://gitee.com/enl-z/typora_-images/raw/master/202212211040058.png)

## Three pieces中的Introduction

### What happens when a program runs?

* Execute instructions (obviously)
  * fetch, decode, and execute

* Others things are happening in the backend

  * make the program to run

  * allow many programs to use/share memory

  * allow may programs to interact with devices

### All about Virtualization

* Virtualization

  * OS transforms the physical resources into easy-to-use virtual form

  * Interaction: system calls - interfaces between program and OS

* Managing: resources manager

### Virtualizing The CPU

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <assert.h>
#include "common.h"
int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        fprintf(stderr, "usage: cpu <string>\n");
        exit(1);
    }
    char *str = argv[1];
    while(1)
    {
        Spin(1);
        printf("%s\n", str);
    }
    return 0;
}
```

### Virtualizing Memory

```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "common.h"

int main(int argc, char *argv[])
{
    int *p = malloc(sizeof(int));
    assert(p != NULL);
    printf("(%d) memory address of p: %08x\n", getpid(), (unsigned) p);
    /* getpid系统调用,打印当前运行程序对应的进程号 */
    *p = 0;
    while(1)
    {
        Spin(1);
        *p = *p + 1;
        printf("(%d) p: %d\n", getpid(), *p);
    }
    return 0;
}
```

### Concurrency | 并发

```c
#include <stdio.h>
#include <stdlib.h>
#include"common.h"
volatile int counter = 0;
int loops;

void *worker(void *arg) 
{
    int i;
    for(i = 0; i < loops; i++) 
    {
        counter++;
    }
    return NULL;
}
int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        fprintf(stderr, "usage: threads <value>\n");
        exit(1);
    }
    loops = atoi(argv[1]);
    pthread_t p1, p2;
    printf("Initial value : %d\n", counter);
    
    Pthread_create(&p1, NULL, worker, NULL);
    Pthread_create(&p2, NULL, worker, NULL);
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("Final value : %d\n", counter);
    
    return 0;
}
```

### I/O

```c
#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <fcntl.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
    int fd = open("/tmp/file", O_WRONLY | O_CREAT | O_TRUNC, S_IRWXU);
    assert(fd > -1);
    intrc = write(fd, "hello world\n", 13);
    assert(rc == 13);
    close(fd);
    return 0;
}
```

