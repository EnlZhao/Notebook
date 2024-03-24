# Anonymous Communication







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

