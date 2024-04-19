# 网络安全原理与实践

本课程主要介绍基本的网络安全攻防手段，具体内容为：

- [x] [DDoS 攻击与防御](ddos.md)：介绍了大量的对称与非对称 DDoS 攻击以及防御手段
- [x] [安全路由](routesec.md)：在回顾计算机网络中学习的路由算法和协议的基础上，基于路由算法的弱点介绍相应的攻击和防御方案
- [x] [匿名通信](anonymity.md)：介绍通过代理节点实现匿名通信的方式，特别是洋葱路由的核心算法，以及相应的攻击手段
- [x] [Web 安全](./websec.md)：介绍 web 基础、SQL 注入、同源策略、跨站攻击等常见的 web 安全问题
- [x] [邮件安全](./mailsec.md)：介绍邮件传输相关的认证算法，核心是邮件的公钥认证体系中的整体架构和关键算法
- [x] [流量分析](./traffic.md)：介绍防火墙、入侵检测系统（IDS）、入侵防御系统（IPS）的原理
- [x] [回溯](./traceback.md)：介绍如何回溯攻击者的身份，如 IP Traceback，Link Testing，Logging-based Traceback 和 Bloom Filter 等方法的原理
- [x] [网络保护](./webprotect.md)：回顾前面章节介绍的防火墙、入侵检测系统（IDS）等内容，同时也介绍负载均衡、用户认证、访问控制等内容

??? info "Three Common properties to protect:"
    - Confidentiality | 保密性 (not leaked to unauthorized parties)
        - Confidentiality refers to protecting information from being accessed by unauthorized parties. In other words, only the people who are authorized to do so can gain access to sensitive data.
    - Integrity | 完整性 (not modified)
        - Integrity is the maintenance of, and the assurance of the accuracy and consistency of, data over its entire life-cycle, aåd is a critical aspect to the design, implementation and usage of any system which stores, processes, or retrieves data.
    - Availability | 可用性 (keep online, available when needed)
        - For any information system to serve its purpose, the information must be available when it is needed. This means the computing systems used to store and process the information, the security controls used to protect it, and the communication channels used to access it must be functioning correctly. High-availability systems aim to remain available at all times, preventing service disruptions due to power outages, hardware failures, and system upgrades. Ensuring availability also involves preventing denial-of-service attacks, such as a flood of incoming messages to the target system, essentially forcing it to shut down.

!!! quote "Acknowledgement"
    - [kaibu](https://list.zju.edu.cn/kaibu/netsec2024/)
    - [咸鱼暄](https://www.yuque.com/xianyuxuan/coding/netsec)
    - [Ryan](https://k5ms77k0o1.feishu.cn/wiki/LLHxwNl7AifNT9kJV17cT0S9noe)