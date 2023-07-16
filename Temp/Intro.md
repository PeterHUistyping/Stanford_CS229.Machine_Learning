Training phase, parameter
```
Email
Hi Chen!   - Spam     (w,c) = (Hi,Spam) (Chen,Spam)
```
```
Email
Hi zhen!   - non-Spam 
```
```
Email
Hi phen!   - Spam    (Hi,Spam) (phen,Spam)
```
-O feature
tokenize 
O={ w1=Hi, w2=Chen, w3=zhen }
P(w1)=1/2,

V=\bigUnion{{w1}}
 
- Class { c1=Spam; c2=non-spam; c3= Middle}

P(c1)=P(Spam)=2/3 
p(c2)=1/3

P(w1|Spam)=2/4    P(w2|spam)=1/4

P(w1|Non-Spam)=1/2 P(w2|nonspam)=0  P(w3='zhen'|spam)=1/2
Test
```
Hi Chen! 
```
cNB=
1. c=spam, Pspam=2/3*2/4
2. c=non-spam, Pspam=0

Problem: data sparsity, P(data wi| unseen class)=0
P(w2|nonspam)=0 


Add-one (Laplace)
(Hi,Spam) (Hi,UnSpam) 
pair default = 1
...

P(w1|Spam)=(2+1)/(4+4)  P(w2|spam)=(1+1)/(4+4)

spam

Hi Zhang!
{w1=Hi, w2=Zhang}
cNB=
1. c=spam, Pspam=2/3*2/4*0
2. c=non-spam, Pspam=0

Problem: data sparsity, P(unseen)=0
Lexicon spam email feature (prize spam free-food  )
intensity, strong, weak


## Data Structure
array
a=[1,2,3]
a[1] O(1)
insert 4 between 1 and 2
for i from 1 to n:
    right-shift 1 position
O(n)
a=[1, ,2,3]
a=[1,4,2,3]

Linked-list dynamic
struct node{
    int value;
    node next;
}

|head ptr
| 1   node | -> | 2 node | -> | 3 node | -> null
get O(n)
insert O(1)





Stack
1 + 2
First in Last out
|   | 
|   |
| 1 | <-

| 2 | <-
| + |
| 1 | 

2 + 1 REVERSE STRING

Queue
FIFO
| C1 C2 C3 .... |

Vector/ Double-ended Queue Deque
|                | 

DICTIONARY / map
(key,value)
dict[k]=5  

pair
('Hi','spam')

dict[('Hi','spam')] = 5 
# count('Hi','spam') = 5


Tree dynamic
struct node{
    int value;
    node left;
    node right;
}
        1
    |       |
    2       3
|
null


def traverse(node ):

BST Binary Search /  B BST  ( Red-black tree -> balance  <-iso-> 2-3tree, B tree t=2 )
        node.left.value < value < node.right.value
        3
    |       |
    2       4 
insert h=O(logn)
first k, O(n)
query 1, O(logn)


Heap
        max-heap
        node.left <  value
        node.right < value
        
        4
    |       |
    3       2
query O(1)



Graph

{vertex:1} -> {vertex:2} -> { 4 }
           -> {v: 3}
v1 : { v2 } linked list
...
vn

     v1  v2  v3  v4
v1 |  0  1
v2 |
v3 |
v4 |

directed ->
undirected <-> sym matrix

Directed Acyclic graph
topological sort
[1 , 2 , 4 , 3]
[1, 4, 2]

traverse graph:
if(visited[v]==false):
    visit(v)
    visit -> true

{vertex:1} -> {vertex:2} -> { 4 }
           -> {v: 3}
stack 
```
visit 1
    visit 2
        visit 4
        prepend list
    visit 3
```
1.neighbour = 2, 3         1=2 -> 3
| 4 |
| 2 |
| 3 |
| 1 |


Initial
```
for v in V:
    visited[v]=false

def visit(node v): 
for v in 1.neighbour
    // only once
    visit(v) # 2 / 3 / ....
```
{vertex:1} -> {vertex:2} -> { 4 }
           -> {v: 3} -> {6}
           -> {v: 5}

only 2: breath-first 4  

visit 1
2, 3, 5
    visit 2
    | 3 5 4 |
    visit 3
    | 5 4 6 |
    visit 3
    visit 4

dijsktra
{vertex:1} -1> {vertex:2} -2> { 4 }
           -2> {v: 3} -3> {6}
           -3> {v: 5}

| 2 {1}, 3{2} , 5{3} |
2 <- min greedy (proof)

dp
