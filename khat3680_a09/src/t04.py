"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-04-03"
-------------------------------------------------------
"""
from BST_linked import BST

bst = BST()

num = [4,2,9,3,6]

for i in num:
    bst.insert(i)

print(bst.node_counts())
print(bst.__contains__(2))
print(bst.parent(2))
print(bst.parent_r(2))