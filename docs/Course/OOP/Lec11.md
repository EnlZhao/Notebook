---
date: 2023-06-28 18:00
---

# Class Design

!!! note "Designing classes"
    How to write classes in a way taht they are easily understandable, maintainable, and reusable

## Software changes

* Software is not like a novel that is written once and then remains unchanged
* Software is <u>extended, corrected, maintained, ported, adapted</u> ...

* There are only two options for software
    * It is <u>dead</u>
    * It is <u>changing</u>
* Software that cannot be maintained will be thrown away

## Code quality

* Two important concepts for quality of code:
    * Coupling
    * Cohesion

### Coupling | 耦合

* Coupling refers to links between separate units of a program
* If two classes depend closely on many details of each other, they are said to be *tightly coupled*
* We aim for *loosely coupled* 

!!! note "Loose coupling"
    Loose coupling makes it possible to:
      * understand one class without reading others
      * change one class without affecting others
      * Thus: improve maintainability

!!! success "tech. to achieve loose coupling"
    1. call-back --- 发消息定义一个接口，另一方可以通过这个接口注册一个回调函数，当发消息时调用其回调函数从而通知自己这件事情发生了
    2. message mechanism --- 实现中央消息机制，把事情发给中央，中央再发布给注册者

### Cohesion | 内聚

* Cohesion refers to the number and diversity of tasks that diversity of tasks that a single unit is responsible for
* If each unit is responsible for one single logical task, we say it has *high cohesion*
* Cohesion applies to classes and methods
* We aim for *high cohesion*

> 让一个单元只复杂一件事情，小到变量，大到模块···

!!! note "High cohesion"
    High cohesion makes it easier to:
        * understand a class or method
        * use descriptive names
        * reuse classes or methods

???+ info "Code duplication | 代码重复"
    * is an indicator of bad design
    * makes maintenance harder
    * can lead to introduction of errors during maintenance

### Responsibility-driven design | 责任驱动设计

* Question: where should we add a new method(which class)?
* Each class should be responsible for manipulating its own data
* The class that owns the data should be responsible for processing it
* RDD leads to low coupling and high cohesion

### Localizing changes | 局部化变化

* One aim of reducing coupling and responsibility-driven design is to localize changes
* When a change is needed, as few classes as possible should be affected

> 可扩展性（extensibility） --- 代码不需要修改（or 很少的修改）就可以满足未来的需求

### Refactoring | 重构

!!! abstract "Code refactoring 是什么"
    在不改变软件的外部行为的条件下，通过修改代码改变软件内部结构，将效率低下和过于复杂的代码转换为更高效、更简单的代码

* Advantages:
    * 提高代码质量
    * 优化软件产品架构与性能
    * 减少项目的技术债，避免项目重写
* Disadvantages:
    * 增加工作负担
    * 可能出现一些业务上的漏洞
    * 可能代码过于精炼导致代码可读性变差

> 重构 != 重写

