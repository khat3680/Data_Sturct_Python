"""
-------------------------------------------------------
[program 1]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-25"
-------------------------------------------------------
"""

from BST_linked import BST

bst1 = BST()
bst2 = BST()

bst1.insert(3)
bst1.insert(4)
bst1.insert(1)
bst1.insert(5)
bst1.insert(9)
bst1.insert(2)

bst2.insert(6)
bst2.insert(4)
bst2.insert(7)
bst2.insert(2)
bst2.insert(3)
bst2.insert(1)

empty = bst1.is_empty()
print(empty)

is_valid = bst1.is_valid()
print(is_valid)

is_identical = bst1.is_identical(bst2)
print(is_identical)

mini = bst1.min()
print(mini)

leaf_count = bst1.leaf_count()
print(leaf_count)

one_child_count = bst1.one_child_count()
print(one_child_count)

two_child_count = bst1.two_child_count()
print(two_child_count)

inorder = bst1.inorder()
print(inorder)

postorder = bst1.postorder()
print(postorder)

levelorder = bst1.levelorder 
print(levelorder)

remove = bst1.remove(4)
print(remove)