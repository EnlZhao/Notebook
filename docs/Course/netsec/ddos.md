---
date: 2024-03-03 19:00
---

# DDos 

## Dos | Denial of Service

- **DoS** (Denial of Service) 攻击是一种网络攻击，目的是使目标系统或网络资源无法提供服务
- 即控制一个机器，向目标机器发送大量的请求以 overload 目标机器，使其无法处理合理的请求（e.g., 卖当劳派大量自家员工去坑德基点东西，但是不买单且处处刁难，使得坑德基无法正常服务真正的顾客）
- defence: block the attacking device

## DDoS | Distributed Denial of Service

> 在 DoS 攻击中，攻击者使用单个系统向目标系统发送大量请求。在 DDoS 攻击中，攻击者使用多个系统向目标系统发送大量请求。使得仅仅通过阻止攻击者的 IP 地址无法阻止攻击。

### Symmetric DDoS Attack

#### Ping Flood

在 Ping Flood 攻击中使用的互联网控制信息协议 (ICMP) 是网络设备用于通信的互
联网层协议。网络诊断工具 traceroute 和 ping 都使用 ICMP 操作。通常情况下， ICMP 回波请求和回波回复信息用于 ping 网络设备，目的是诊断设备的健康状况和连接性，以及发送者和设备之间的连接。
一个icmp请求需要一些服务器资源来处理每个请求和发送响应。该请求还需要传入
信息（回音请求）和传出响应（回音响应）的带宽。

pingflood是一种网络攻击，它利用了ping命令来向目标主机发送大量的ping请求。
从而使目标主机过载或崩溃。攻击者通过发送大量的ping请求，使目标主机不断地响
应请求，从而导致网络拥塞和服务质量下降。pingflood攻击通常是 ddos 的一种形式。
pingflood攻击的目的是压倒目标设备对大量请求的响应能力和/或用虚假流量使网络
连接过载。通过让僵尸网络中的许多设备用icmp请求瞄准同一个互联网财产或基础
设施组件，攻击流量大大增加，有可能导致正常的网络活动中断。历史上，攻击者通。
常会伪造一个假的ip地址，以掩盖发送设备。在现代僵尸网络攻击中，恶意行为者很
少认为有必要掩盖僵尸的ip,而是依靠一个由未被欺骗的僵尸组成的大型网络来使目
标的容量饱和。
ping(icmp)flood dos形式可以分解为两个重复的步骤。
攻击者使用多个设备向目标服务器发送许多icmp回波请求包。
然后，目标服务器向每个请求设备的ip地址发送一个icmp回波数据包作为回应。

- ICMP Echo
- Echo request & response consume bandwidth
- 消耗其响应能力 或者 网络带宽
- 解决：禁用 ICMP (ping / tracert / etc.)

#### TCP SYN Flood

Single machine:

- SYN packets with random source IP addresses
- Fill up backlog queue on server
- No further connections possible

IP Spoofing:

- SYN packets with random source IP addresses
- Fill up backlog queue on server
- No further connections possible

IP Spoofing: Craft SYN packets from randomly forged IP address;
For such random IP addresses, after they receive SYN ACK packets from the server, they may simply discard them as these IP addresses have not sent SYN requests at all

Queue size: commonly set as 128 by default on some Linux systems;

Timeout: evict a backlog entry if no ack is received until timeout, e.g., 3 mins 

Attack example: attacker sends 128 SYN every 3 mins without responding with ACK pkts

Attack principle

- server commits resources (memory) before confirming identify of client (when client responds)

Solution?

1. increase backlog queue size
    - **but** attacker can sends more SYN packets!
2. decrease timeout 
    - **but** interrupt normal service requests!
3. **SYN cookies**
    - Goal: avoid state storage on server until 3-way handshake completes
    - Idea: 
        - server sends necessary states to client along with SYN-ACK;
        - client sends these states back to server along with ACK;

在 client 发送给 server 的 SYN 包后，相比之前的 TCP handshake, server 不再保存 client 的 SN~C~ 包，而是将 client 的信息加密后发送给 client 自己的 SN~S~ 包，其中 SN~S~ = (T || M || L) (Total 32 bits)
- T: 5-bit timestamp time() logically right-shifted 6 positions; 64-second resolution
- M: 3-bit MSS (maximum segment size)
- L: 24-bit keyed hash, L = MAC~key~ (SAddr, SPort, DAddr, DPort, SN~C~, T)

server 收到 client 发回的 ack 包后，复原 SN~C~ 和 SN~S~，之后核验 SN~S~ 即可判断是否是合法的 client

![SYN Cookies](../../Images/2024-03-03-20-33-55.png)

TCP SYN Flood Backscatter: 指 server 接收到 Spoofed IP 的 SYN 后发回的 SYN + ACK 包

- 伪造的 IP 地址收到 server 发的 SYN + ACK 后，不会回复（因为并非那个 IP 真正发的），以此来检测 DDos
- For detection: Since syn flood uses forged source IP, then responses to those forged IPs get no further responses;


### Asymmetric DDoS Attack




## Some Questions

??? question "What is the difference between DoS and DDoS?"
    - DoS attack - Denial of Service attack. The attacker overload victim by exhausting its resources (bandwidth, computing resources or queue spaces), making it unable to response for some normal legal requests.
    - DDoS attack - Distributed DoS attack. The attacker use a large amount of devices to perform DoS attack on a victim, in the same way and for the same results. 
    - The difference is that, DDoS attackes are performed by many devices which are usually in different subnets. If DoS attack is performed by a single device, the victim can easily defend it by blocking its IP or subnet, but as for DDoS attack, the attacking devices are widely distributed, so it's kind of hard to defend.

??? question "How does the TCP SYN Flood attack work?"
    When we send a SYN (1st handshake) to the victim, it will allocate some resources to save informations like the SEQ of the coming packet, and this packet will be pushed into SYN queue (SYN backlog). However, the SYN queue is small, normally 128 entries. If the attacker only send SYN but not response to the SYN+ACK (2nd handshake) segment, then the SYN packet will be stored in the queue until the time is exceeded, which is normally 3 minutes. So if the attacker send no less than 128 SYN packet each 3 minutes without responsing to any SYN+ACK packet, the SYN backlog of the victim will always be full and the legal requests of other devices will not be fulfilled, resulting in a Denial of Service.

??? question "How does the solution of SYN Cookies against TCP SYN Flood attacks work?"
    We can see from the principle of TCP SYN Flood that, the weakness is the limitation of SYN queue. The aim of this queue is to store the information of the coming SYN packets, so we can find ways to avoid this kind of storage. Instead, SYN Cookies try to hide the information of the SYN packets into the SYN+ACK packet. As we know, the 3 steps of TCP handshake is to exchange their initial sequence, which is related to time. But if SYN Cookies is used, the sequence of SYN+ACK packet sent by the server is a digest of the data of SYN packet and other information like time. When the ACK (3rd handshake) comes, it can check its acknowledge number and know whether it is legal. In this way, the SYN queue is not needed, so the TCP SYN Flood attack will not work.

??? question "How does the DNS Amplification Attack work? How to defend against it?"
    - DNS Amplification Attack uses open DNS resolvers, which provide an open DNS service for all internet users. The attacker uses a spoofed IP address which is actually the IP address of the victim to send a query to the open DNS resolver, and it will send a response to the victim. There is a kind of DNS request `ANY`, which will return all types of information of a given name, which is a huge amount of data. 
    - Defense: reduce the number of open DNS solvers, or disable the `ANY` request of them, or use techniques like ingress filtering, or disable UDP service of the victim.

??? question "How does Memcached attack work?"
    Memcached attack uses memcached servers, which provide (distributed) cache service for speeding up website accessing. Memcached services also use UDP so there is no need to setup a connection. The attacker pre-load the memcached server with some related information with methods like accessing it, and then send a request to the memcached server with spoofed IP address which is actually the IP address of the victim. The server will then send a very large amount of data to the victim, and the victim will be overwhelmed.

??? question "What is the difference between HTTP Flood and Fragmented HTTP Flood?"
    - HTTP Flood mainly exhausts the server by GET or POST some large contents, and the server will need to take them from or store them into database, which is time consuming; the server may also need to encrypt or decrypt the contents, which will consume the computing resources of the server.
    - Fragmented HTTP Flood trys to split a HTTP segment into many small fragments, and to send it very slowly but not exceed the timeout, so that the server will always keep the connection which is resource consuming.

??? question "Why is Fragmented HTTP Flood relatively more challenging to detect?"
    Because the content, traffic and source are very normal. For other DDoS attacks, there are useless large-scale data or abnormal requests, which is easy to detect. But Fragmented HTTP Flood looks just like a normal user.

??? question "How does Ingress Filtering work?"
    Ingress Filtering asks the source ASes to check each packet before routing them on the public net whether the source IP address is in the subnet of the outcoming AS. If not, this packet should not be routed.

??? question "How does IP Traceback work?"
    - Some information should be added into the packet so that the receiver can check whether the path is valid.
    - The easiest way is to add all the path information into the packet, but it will make the packet too large.
    - Another way is use edge sampling, by using propability, each packet will sample different routers on the way as well as a distance to the sampled router. As a session will normally send many packets, we can restore she whole path.