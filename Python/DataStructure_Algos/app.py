from Binary_Tree import BinaryTree
from Node import Node

head = Node(20)
bT = BinaryTree(head)

lst = [10, 30, 5, 15, 25, 35, 3, 7, 17, 27, 37, 39, 2, 1]

for i in lst:
    bT.add_node(i)

x = bT.get_head()

bT.communicateToEmployees(x)
