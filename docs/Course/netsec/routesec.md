# Secure Routing

!!! bug "routing attacks"
    - distance-vector: announce 0 distance to all other nodes
    - link-state: drop links; claim direct link to other routers
    - BGP: announce arbitrary prefix; alter paths

Deliver Scheme:

- `unicast` delivers a message to a single specific node
- `broadcast` delivers a message to all nodes in the network
- `multicast` delivers a message to a group of nodes
- `anycast` delivers a message to any one out of a group of nodes, typically the one nearest to the source
- `geocast` delivers a message to a group of nodes based on **geographic location**

> Unicast is the dominant form of message delivery on the Internet. 

Routing Scheme:

- Intra-domain routing: inside an autonomous system (AS)
- Inter-domain routing: between different ASs

## Route Computation

