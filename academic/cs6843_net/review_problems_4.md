# Review Problem Set 4

#####R2. What are the two most important network-layer functions in a datagram network? What are the three most important network-layer functions in a virtual-circuit network?

- Datagram-based network layer: forwarding; routing. Additional function of VC-based network layer: call setup.

#####R9. Describe how packet loss can occur at input ports. Describe how packet loss at input ports can be eliminated (without using infinite buffers).

- If the rate at which packets arrive to the fabric exceeds switching fabric rate, then packets will need to queue at the input ports. If this rate mismatch persists, the queues will get larger and larger and eventually overflow the input port buffers, causing packet loss. Packet loss can be eliminated if the switching fabric speed is at least n times as fast as the input line speed, where n is the number of input ports.


#####R10. Describe how packet loss can occur at output ports. Can this loss be prevented by increasing the switch fabric speed?

- Assuming input and output line speeds are the same, packet loss can still occur if the rate at which packets arrive to a single output port exceeds the line speed. If this rate mismatch persists, the queues will get larger and larger and eventually overflow the output port buffers, causing packet loss. Note that increasing switch fabric speed cannot prevent this problem from occurring.


#####R13. What is the 32-bit binary equivalent of the IP address 223.1.3.27?

- 11011111 00000001 00000011 00011011.

#####P2. Consider a virtual-circuit network. Suppose the VC number is an 8-bit field.
- a. What is the maximum number of virtual circuits that can be carried over a link?
- b. Suppose a central node determines paths and VC numbers at connection setup. Suppose the same VC number is used on each link along the VC’s path. Describe how the central node might determine the VC number at connection setup. Is it possible that there are fewer VCs in progress than the maximum as determined in part (a) yet there is no common free VC number?
- c. Suppose that different VC numbers are permitted in each link along a VC’s path. During connection setup, after an end-to-end path is determined, describe how the links can choose their VC numbers and configure their forwarding tables in a decentralized manner, without reliance on a central node.

- Maximum number of VCs over a link 2**8 = 256.
- The centralized node could pick any VC number which is free from the set {0,1,…,2**8-1}. In this manner, it is not possible that there are fewer VCs in progress than 256 without there being any common free VC number.
- Each of the links can independently allocate VC numbers from the set {0,1,…,2**8-1}. Thus, a VC will likely have a different VC number for each link along its path. Each router in the VC’s path must replace the VC number of each arriving packet with the VC number associated with the outbound link.

#####P21. Consider the network setup in Figure 4.22. Suppose that the ISP instead assigns the router the address 24.34.112.235 and that the network address of the home network is 192.168.1/24.
- a. Assign addresses to all interfaces in the home network.
- b. Suppose each host has two ongoing TCP connections, all to port 80 at host 128.119.40.86. Provide the six corresponding entries in the NAT translation table.

#####P26. Consider the following network. With the indicated link costs, use Dijkstra’s shortest-path algorithm to compute the shortest path from x to all network nodes. Show how the algorithm works by computing a table similar to Table 4.3.
```
Step N’ D(t),p(t) D(u),p(u) D(v),p(v) D(w),p(w) D(y),p(y) D(z),p(z)
0 x ∞ ∞ 3,x 6,x 6,x 8,x
1 xv 7,v 6,v 3,x 6,x 6,x 8,x
2 xvu 7,v 6,v 3,x 6,x 6,x 8,x
3 xvuw 7,v 6,v 3,x 6,x 6,x 8,x
4 xvuwy 7,v 6,v 3,x 6,x 6,x 8,x
5 xvuwyt 7,v 6,v 3,x 6,x 6,x 8,x
6 xvuwytz 7,v 6,v 3,x 6,x 6,x 8,x
```

#####P28. Consider the network shown below, and assume that each node initially knows the costs to each of its neighbors. Consider the distance-vector algorithm and show the distance table entries at node z.

#####P30. Consider the network fragment shown below. x has only two attached neighbors, w and y. w has a minimum-cost path to destination u (not shown) of 5, and y has a minimum-cost path to u of 6. The complete paths from w and y to u (and between w and y) are not shown. All link costs in the network have strictly positive integer values.
- a. Give x’s distance vector for destinations w, y, and u.
- b. Give a link-cost change for either c(x,w) or c(x,y) such that x will inform its neighbors of a new minimum-cost path to u as a result of executing the distance-vector algorithm.
- c. Give a link-cost change for either c(x,w) or c(x,y) such that x will not inform its neighbors of a new minimum-cost path to u as a result of executing the distance-vector algorithm.


#####P37. Consider the network shown below. Suppose AS3 and AS2 are running OSPF for their intra-AS routing protocol. Suppose AS1 and AS4 are running RIP for their intra-AS routing protocol. Suppose eBGP and iBGP are used for the inter-AS routing protocol. Initially suppose there is no physical link between AS2 and AS4.
- a. Router 3c learns about prefix x from which routing protocol: OSPF, RIP, eBGP, or iBGP?
- b. Router 3a learns about x from which routing protocol?
- c. Router 1c learns about x from which routing protocol?
- d. Router 1d learns about x from which routing protocol?


#####P38. Referring to the previous problem, once router 1d learns about x it will put an entry (x, I) in its forwarding table.
- a. Will I be equal to I1 or I2 for this entry? Explain why in one sentence.
- b. Now suppose that there is a physical link between AS2 and AS4, shown by the dotted line. Suppose router 1d learns that x is accessible via AS2 as well as via AS3. Will I be set to I1 or I2? Explain why in one sentence.
- c. Now suppose there is another AS, called AS5, which lies on the path between AS2 and AS4 (not shown in diagram). Suppose router 1d learns that x is accessible via AS2 AS5 AS4 as well as via AS3 AS4. Will I be set to I1 or I2? Explain why in one sentence.


#####P44. Consider the seven-node network (with nodes labeled t to z) in Problem P26. Show the minimal-cost tree rooted at z that includes (as end hosts) nodes u, v, w, and y. Informally argue why your tree is a minimal-cost tree.
