# Anonymous Communication

对于 Internet 中交流的双方 ip1 和 ip2, 如果有一个 attacker snooping on the communication, 尽管它可能不知道两个用户的身份，也无法知道他们被加密的通信内容。但它起码可以使用他们的 ip

> Because, for users to communicate via internet, their devices assigned with IP addresses, which are usually fixed within a communication session or more;
> 
> This can be used to infer critical privacy of users

??? note "Communication anonymity & privacy:"
    - who is communicating?
    - who are you talking to?
    - what type of activities?
    - what type of information?

**1) Why wanted?**

=== "Anonymity for Mortals"
    - Unmonitored access to health and medical information
    - Preservation of democracy: anonymous election/jury
    - Censorship circumvention: anonymous access to otherwise restricted information
=== "Anonymity for Attackers"
    Misbehaviors without getting caught: Terrorism, Darknet, Spam, Pirate...

**2) how to?**

通过加密（如 HTTPS）可以保护访问的内容；

> But even if we don’t know what you communicated, knowing with whom you communicated leaks a lot of information as well

Thus, we can **hide destination address**

But here comes another question: 

- According to routing, need to specify the ip address of destination to ensure packets being directed toward it,
- Then how to deliver packets to destination? $\rightarrow$ **RELAY!**

??? abstract "Relay"
    - Relay (中继) 常指一种网络设备或服务，可以用于 <u>转发</u> 数据包或信息, 以帮助连接不同的子网或网络。
    - 中继可以帮助解决网络通信中的距离限制和协议转换问题，进而扩大网络的覆盖范围和功能。
    - 中继可以分为物理中继和逻辑中继两种类型。
        - 物理中继是指一种网络设备或链路，它用于将数据包从一个物理网络转发到另一个物理网络。比如，网络交换机、路由器、网关等设备。
        - 逻辑中继是指一种软件或服务，它用于将数据包从一个逻辑网络转发到另一个逻辑网络。比如，代理服务器、VPN 网关、DNS 中继等服务。

Here comes **Overlay Communication**

## Overlay Communication

!!! abstract "Overlay Communication"
    - Overlay Communication（覆盖通信）是一种在网络中添加虚拟网络层的技术，用于改进网络性能和扩展网络功能。
    - 通过覆盖通信，可以在现有的网络架构上增加一个虚拟的网络层，这个虚拟层与底层网络相互独立，可以实现更高效、更安全和更灵活的通信方式。​

![](../../Images/2024-03-27-16-38-26.png)

其中 ip3 是一个 relay node

### Overlay Network

![](../../Images/2024-03-27-16-45-56.png)

覆盖通信的主要思想是，在应用层和传输层之间添加一个 **中间层**，这个中间层可以通过使用不同的协议、路由和拓扑结构来优化网络通信。

在覆盖通信中，应用程序会将数据包发送到覆盖网络中，然后由覆盖网络负责将数据包传输到目标地址，从而实现更快速、更可靠的通信。

!!! warning "Threat Model"
    这里定义攻击模型：Insider Byzantine Attacker

    - Insider 表示攻击者本身是网络的一部分（ASes, 攻击者可能控制不止一个 ASes）但攻击者没有能力知道整个网络 (limited view of network)
    - Byzantine 表示一种攻击模式，攻击者的的攻击行为是不稳定的（长期、一致的攻击会容易被发现，因此攻击者采取间断式的、不同方式的攻击，就比较难被检测到了）

    攻击者的目标是：在目的 IP 信息隐藏在数据包中的情况下，得知数据包的最终目的地。

由此提出两种攻击行为：

1. Traceforward Attack
      - passive attacker
      - traces messages from sender, thwarts receiver anonymity
      - 被动攻击者跟踪数据包信息
2. Marking Attack
      - active attacker
      - marks messages, discovers marked msg elsewhere
      - 攻击者比较厉害，可以改经过它的数据包，那可以加个标记，然后在其他地方发现就知道是发过来了

## Anonyminzing Proxy

- intermediary between sender & receiver
- Sender relays all traffic through proxy
- Encrypt destination and payload
- Asymmetric technique: receiver not involved (or informed of) anonymity

![](../../Images/2024-03-27-17-30-04.png)

k: shared key of sender and proxy

1. 如果攻击者在 sender 和 proxy 之间监听，那么 sender 丧失了匿名性
2. 如果攻击者在 proxy 和 receiver 之间监听，那么 receiver 丧失了匿名性
3. 如果有两个攻击者，一个在 sender 和 proxy 之间，一个在 proxy 和 receiver 之间，两者串通比对 ingress 和 egress 的流量，则 sender 和 receiver 都丧失了匿名性
4. 如果 proxy 本身是恶意的，那么 sender 和 receiver 都丧失了匿名性

### what if receiver is attacker

> 需要保护发送者的匿名性

![](../../Images/2024-03-27-17-36-07.png)

### 优缺点

- Advantages:
    - Easy to configure
    - Require no active participation of receiver, which need not be aware of anonymity service
    - Have been widely deployed on Internet
- Disadvantages:
    - Require trusted third party proxy may release logs, or sell them, or blackmail sender
    - Anonymity largely depends on the (likely unknown) location of attacker

### How to evade attackers?

> dynamic proxy location

Here comes **Crowds Algorithm**

- Basic idea: get lost in a crowd
- Jump from one crowd to another
- Members of a crowd called Jondos
- Algorithm:
    - Relay message to random jondo
    - With probability p, jondo forwards message to another jondo
    - With probability 1-p, jondo delivers message to its intended destination

![](../../Images/2024-03-27-17-44-16.png)

### How to evade untrusted proxies?

**proxy ++**

多弄一些 proxy, 用于混淆攻击者的视线

Its hard for an attacker to **simultaneously** control too many proxies

Other methods: 

#### Source Routing

!!! abstract
    - specify on-path routers by source
    - allows a sender of a packet to partially or completely specify the route the packet takes through the network.
    - In contrast, in conventional routing, routers in the network determine the path incrementally based on the packet's destination

Source Routing / Path Addressing 允许发送者指定一个包的部分或者全部路由​

源路由技术中，数据包的路由路径是在数据包的头部中指定的，这意味着发送方可以选择数据包的路由路径，而不是让网络中的路由器根据它们的路由表来自动选择。

#### POF-based Source Routing

> POF: Protocol Oblivious Forwarding

![](../../Images/2024-03-27-17-48-47.png)



## Some Questions

??? question "Why is current Internet communication vulnerable to anonymity or privacy leakage? "
    Because Internet uses IP address to identify a host, and each router on the path from source to destination needs to know about the exact IP address of the destination to make the routing decision. But the IP address itself as well as the communication source and destination can leak some anonymity and privacy, because knowing the existance of communication without the exact contents is enough to infer some information on the user, who is easy to find by its IP address.

??? question "In which scenarios do users require the communication anonymity or privacy as concerned in sub-question a?"
    There are cases where users try to access some medical, voting or other kind of information related to privacy. If one is known to usually access the website of a party or candidate, he is inclined to vote for the candidate, which is a privacy leakage. Also, when an attacker is trying to spy on or modify some data, he is also not willing to be known about his IP address, which can find him easily.

??? question "How to use proxies to secure communication anonymity? What are the possible limitations?"
    - The sender send message to the proxy instead of the destination, and the destination is encrypted and placed in the packet. The proxy will decrypt it and send the corresponding message to the destination. If the attacker sniffs between the sender and proxy, he will not know about the destination, and if it sniffs between the proxy and destination, he will not know about the source.
    - However, if the attacker sniffs both between the sender and proxy, and between the proxy and destination, the anonymity will fail. So will it fail in the case where the proxy itself is malicious.

??? question "How does Onion Routing provide a better guarantee for anonymity?"
    The proxy nodes are randomly selected and each node can only decrypt one layer and will encrypt when it pass to next node. Unless there are enough number of nodes collude with each other, they know nothing about the source or destination.

??? question "How to infer anonymity or privacy of Onion Routing traffic?"
    Each node only knows about the immediately preceding and following node in a relay. The source and destination of messages is obscured by layers of encryption. And because of the layers of encryption and randomization, none of the nodes can know whether the next and last node is the source or destination or not.

