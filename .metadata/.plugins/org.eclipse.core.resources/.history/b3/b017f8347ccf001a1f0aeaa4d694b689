"""
-------------------------
# Student Name: Pranav Verma
# Student ID:193272030
# Student email:verm2030@mylaurier.ca
#-------------------------
"""

from copy import deepcopy
from operator import __eq__

from ad import Queue
from stack import Stack


class BSTNode:
    """
    ----------------------------------------------
    Implementation of a Binary Search Tree node
    ----------------------------------------------
    """

    def __init__(self, value):
        """
        -------------------------------------------------------
        Description:
            Creates and initializes a binary search tree node
            data is set to given values
            left and right pointers are set to None
            height is set to 1
        Assert: none
        Use: my_node = Node()
        -------------------------------------------------------
        Parameters:
            item: An arbitrary object (?)
        Returns:
            An object of type BSTNode 
        -------------------------------------------------------
        """ 
        self._data = deepcopy(value)
        self._left = None
        self._right = None
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns string representation of BSTNode
            Used for testing purposes
        Assert: none
        Use: str(my_node) or print(my_node)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string represenation of BSTNode
        -------------------------------------------------------
        """
        return str(self._data)

    def height(self):
        """
        -------------------------------------------------------
        Description:
            Returns the height of the node
            height = 1 + max(left_node_height,right_node_height)
            if node is None returns 0
        Assert: none
        Use: h = node.height()
        -------------------------------------------------------
        Parameters:
            none
        Returns:
            h: height of node (int)     
        -------------------------------------------------------
        """
        return self._height_aux(self)
        
    def _height_aux(self, node):
        """
        -------------------------------------------------------
        Description:
            Private helper function that computes the height of a node
        Assert: none
        Use: h = self._height_aux(node)
        -------------------------------------------------------
        Parameters:
            node: a bst node (BSTNode)
        Returns:
            h: height of node (int)     
        -------------------------------------------------------
        """
        if node is None:
            return 0
        return 1 + max(self._height_aux(node._left), self._height_aux(node._right))

        
class BST:
    """
    ----------------------------------------------
    Implementation of Binary Search Tree
    ----------------------------------------------
    """
    MAX_SIZE = 1000

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Initializes an empty binary search tree
            root is set to None and count to 0
        Assert: none
        Use: bst = BST()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type BST
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0
        
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of bst
            Uses Breadth First Search (BFS)
        Assert: none
        Use: str(bst) or print(bst)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of bst (str)
        -------------------------------------------------------
        """
        q = Queue(self.MAX_SIZE)
        output = ''
        q.insert(self._root)
        level = 1
        while not q.is_empty():
            node = q.remove()
            if node is None:
                continue
            node_level = self.level(node._data)
            if node_level == level:
                output += str(node._data) + " "
            elif node_level > level:
                output = output[:-1] + "\n"
                output += str(node._data) + " "
                level += 1
            if node._left is not None:
                q.insert(node._left)
            if node._right is not None:
                q.insert(node._right)
        return output[:-1]            
    
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Check if bst is empty
        Assert: none
        Use: result = bst.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if bst is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        return self._root is None
            
    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Returns number of items in a bst
            same as number of nodes
        Assert: none
        Use: length = len(bst)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in bst       
        -------------------------------------------------------
        """
        return self._count
        
    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for given key in bst
            returns reference to node and its parent
            If not found returns None,None
        Assert: none
        Use: parent,node = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            parent: reference to the parent of the node containing key (BSTNode)
            node: reference to the node containing the key (BSTNode)
        -------------------------------------------------------
        """
        if key is  None:
            return None, None
        parent = None
        node = self._root
        while node is not None and key != node._data:
            parent = node
            if key > node._data:
                node = node._right
            else: 
                node = node._left
        if node is None:
            parent = None
        return parent, node      
    
    def find(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds and returns(retrives) a copy of item in bst that matches key.
            If item not found returns None
        Assert: none
        Use: item = bst.find(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        _, node = self._binary_search(key)
        if node is None:
            return None
        return deepcopy(node._data)
    
    def insert(self, item):
        """
        -------------------------------------------------------
        Description:
            inserts a copy of given item into bst
            Duplicates not allowed
            if insertion is successful, returns True, otherwise False
        Assert: none
        Use: success = bst.insert(item)
        -------------------------------------------------------
        Parameters:
            item - an item to be added (?)
        Returns:
            success: True/False (bool)     
        -------------------------------------------------------
        """
        return self._insert_aux(self._root, item)

    def _insert_aux(self, node, item):
        """
        -------------------------------------------------------
        Description:
            Private helper function for insert method
            inserts a copy of given item into node
            Uses recursion
        Assert: none
        Use: success = self._insert_aux(node,item)
        -------------------------------------------------------
        Parameters:
            node - a bst node (BSTNode)
            item - an item to be added (?)
        Returns:
            success: True/False (bool)     
        -------------------------------------------------------
        """
        if self._root is None:
            self._count += 1
            self._root = BSTNode(deepcopy(item))
            return True
        if item == node._data:
            return False
        if item > node._data:
            if node._right is None:
                self._count += 1
                node._right = BSTNode(deepcopy(item))
                return True
            return self._insert_aux(node._right, item)
        if node._left is None:
            self._count += 1
            node._left = BSTNode(deepcopy(item))
            return True
        return self._insert_aux(node._left, item)

    def height(self):
        """
        -------------------------------------------------------
        Description:
            Returns the height of a tree
            height of tree is the height of its root node
        Assert: none
        Use: h = bst.height()
        -------------------------------------------------------
        Parameters:
            none
        Returns:
            h: height of tree (int)     
        -------------------------------------------------------
        """
        if self._root is None:
            return 0
        return self._root.height()
    
    def level(self, key):
        """
        -------------------------------------------------------
        Description:
            Returns the level of the given key in the bst
            if not found, prints error message and returns -1
        Assert: none
        Use: l = bst.level(key)
        -------------------------------------------------------
        Parameters:
            key: partial data to search for
        Returns:
            l: level of given key (int)
        -------------------------------------------------------
        """
        _, node = self._binary_search(key)
        if node is None:
            print('Error(get_level):key not found')
            return -1
        return self._get_level_aux(self._root, node, 1)
        
    def _get_level_aux(self, start, node, level):
        """
        -------------------------------------------------------
        Description:
           A private helper method method for level()
           Uses recursion to find level of given node compared to start node
        Assert: none
        Use: l = self._get_level_aux(start,node,starting_level)
        -------------------------------------------------------
        Parameters:
            start: node acting as a root of subtree (BSTNode)
            node: current node being examined to determine level (BSTNode)
            level: level of starting node
        Returns:
            l: level of node (int)
        -------------------------------------------------------
        """
        if start is None:
            return -1
        if start._data == node._data:
            return level
        new_level = self._get_level_aux(start._left, node, level + 1)
        if new_level != -1:
            return new_level
        else:
            return self._get_level_aux(start._right, node, level + 1)
        
    def is_descendant(self, key1, key2):
        """
        -------------------------------------------------------
        Description:
             Check if key1 is a descendent of key2 in bst
        Assert: None
        Use: result = bst.is_descendent(key1,key2)
        -------------------------------------------------------
        Parameters:
            key1 - partial data (?)
            key2 - partial data (?)
        Returns:
            returns True/False (bool)    
        -------------------------------------------------------
        """
        _, node1 = self._binary_search(key1)
        _, node2 = self._binary_search(key2)
        if node1 is None or node2 is None:
            return False
        if node1 is node2:
            return False
        return self._is_descendant_aux(node1, node2)
    
    def _is_descendant_aux(self, node1, node2):
        """
        -------------------------------------------------------
        Description:
            Private helper function for is_descendant
        -------------------------------------------------------
        """
        if node2 is None:
            return False
        if node2._left is node1 or node2._right is node1:
            return True
        return self._is_descendant_aux(node1, node2._left) or self._is_descendant_aux(node1, node2._right)
    
    def remove(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds, removes, and returns the value in bst that matches key.
            if key not found returns None
            If bst is empty, prints an error message and returns None
        Assert: none
        Use: item = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        if self._root is None:
            print("Error(BST.remove): Cannot remove from any empty bst")
            return None
        self._root, item = self._remove_aux(self._root, key)
        return item

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Preconditions:
            node - a bst node to search for key (_BSTNode)
            key - data to search for (?)
        Postconditions:
            returns
            node - the current node or its replacement (_BSTNode)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            item = None
        elif key < node._data:
            node._left, item = self._remove_aux(node._left, key)
        elif key > node._data:
            node._right, item = self._remove_aux(node._right, key)
        else:
            item = node._data
            self._count -= 1
            if node._left is None and node._right is None:
                node = None
            elif node._left is None:
                node = node._right 
            elif node._left is None:
                node = node._left
            else:
                if node._left._right is None:
                    replacement_node = node._left
                else:
                    replacement_node = self._delete_node_left(node._left)
                    replacement_node._left = node._left
                replacement_node._right = node._right
                node = replacement_node
                    
        return node, item
        
    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Preconditions:
            parent - node to search for largest value (_BSTNode)
        Postconditions:
            returns
            repl_node - the node that replaces the deleted node. This node 
            is the node with the maximum value in the deleted node's left
            subtree (_BSTNode)
        -------------------------------------------------------
        """
        child = parent._right
        if child._right is None:
            replacement_node = child
            parent._right = child._left
        else:
            replacement_node = self._delete_node_left(child)
        return replacement_node
    
    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Postconditions:
            returns
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        return self._leaf_count_aux(self._root)
        
    def _leaf_count_aux(self, node):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: n = bst.leaf_count()
        (Recursive algorithm)
        ---------------------------------------------------------
        Preconditions:
            node - a BST node (_BSTNode)
        Postconditions:
            returns
            count - number of nodes with no children below node (int)
        ---------------------------------------------------------
        """
        if node is None:
            return 0
        if node._left is None and node._right is None:
            return 1
        return self._leaf_count_aux(node._left) + self._leaf_count_aux(node._right)
        
    def __contains__(self, item):
        _, node = self._binary_search(item)
        return node is not None
    
    def is_ancestor(self, key1, key2):
        _, node1 = self._binary_search(key1)
        parent2, node2 = self._binary_search(key2)
        
        if node1  is None or node2 is None:
            return False
        if node1 is self._root:
            return True
        current = parent2
        while current is not self._root:
            if current is node1:
                current = True
            current, _ = self._binary_search(current._data)
        return False
    
    def inorder(self):
        items = []
        self._inorder_aux(self._root, items)
        return items

    def _inorder_aux(self, node, items):
        if node is None:
            return
        self._inorder_aux(node._left, items)
        items.append(deepcopy(node._data))
        self._inorder_aux(node._right, items)
        
    def inorder2(self):
        items = []
        stack = Stack()
        node = self._root
        while not stack.is_empty() or node is not None:
            if node is None:
                node = stack.pop()
                items.append(deepcopy(node._data))
                node = node._right
            else:
                stack.push(node)
                node = node._left
        return items
    
    def preorder(self):
        items = []
        self._preorder_aux(self._root, items)
        return items
    
    def _preorder_aux(self, node, items):
        if node is None:
            return
        items.append(deepcopy(node._data))
        self._preorder_aux(node._left, items)
        self._preorder_aux(node._right.items)
        
    def preorder2(self):
        items = []
        stack = Stack()
        node = self._root
        stack.push(node)
        while not stack.is_empty():
            node = stack.pop()
            items.append(deepcopy(node._data))
            if node._right is not None:
                stack.push(node._right)
            if node._left is not None:
                stack.push(node._left)
        return items
    
    def postorder(self):
        items = []
        self._postorder_aux(self._root, items)
        return items

    def _postorder_aux(self, node, items):
        if node is None:
            return
        self._postorder_aux(node._left, items)
        self._postorder_aux(node._right, items)
        items.append(deepcopy(node._data))
        return
    
    def postorder2(self):
        items = []
        stack1 = Stack()
        stack2 = Stack()
        node = self._root
        stack1.push(node)
        while not stack1.is_empty():
            node = stack1.pop()
            stack2.push(node)
            if node._left is not None:
                stack1.push(node._left)
            if node._right is not None:
                stack1.push(node._right)
        while not stack2.is_empty():
            items.append(stack2.pop()._data)
        return items

    def levelorder(self):
        items = []
        queue = Queue()
        node = self._root
        queue.insert(node)
        while not queue.is_empty():
            node = queue.remove()
            items.append(deepcopy(node._data))
            if node._left is not None:
                queue.insert(node._left)
            if node._right is not None:
                queue.insert(node._right)
        return items

    def __eq__(self, bst2):
        """
        -------------------------------------------------------
        Description:
        Check if given bst is equal to current bst
        All data should be equal and at the same node location
        Assert: bst2 is a BST
        Use: bst1 == bst2
        -------------------------------------------------------
        Parameters:
        bst2 - a binary search tree to compare with (BST)
        Returns:
        True/False
        -------------------------------------------------------
        """
        if self._root == None and bst2._root == None:
            return True
        if(self._root != None and bst2._root == None):
            return False
        if self._root == None and bst2._root != None:
            return False  
        # else:
            # if(self._leaf_count() != bst2._leaf_count()):
                # return False
        if((self._root._data == bst2._root._data) and __eq__(self._root._left, bst2._root._left) and __eq__(self._root._right, bst2._root._right)):
            return True
        else:
            return False
        
#         if (root1 == None and root2 == None) : 
#         return 1
#           
#     # If any one of the tree is non-empty  
#     # and other is empty, return false  
#     elif (root1 != None and root2 == None) : 
#         return 0
#     elif (root1 == None and root2 != None) : 
#         return 0
#     else: # Check if current data of both trees  
#           # equal and recursively check for left  
#           # and right subtrees  
#         if (root1.data == root2.data and 
#             isIdentical(root1.left, root2.left)  
#             and isIdentical(root1.right, root2.right)) : 
#             return 1
#         else: 
#             return 0
    def _is_valid_aux(self, node):
        if node is None:
            valid = True
        elif node._right is not None and node._right._data <= node._data:
            valid = False
        elif node._height != max(self._node_height(node._left), self._node_height(node._right)) + 1:
            valid = False
        else:
            valid = self._is_valid_aux(node._left) and self._is_valid_aux(node._right)
        return valid

    def is_valid(self):
        """
        -------------------------------------------------------
        Description:
        Determines if BST is a true BST
        Basic property of BST is that for any node
        - all nodes in the left subtree are smaller
        - all nodes in the right subtree are larger
        Returns True if above property is satisfied, False otherwise
        Assert: none
        Use: result = bst.is_valid()
        -------------------------------------------------------
        Parameters:
        None
        Returns:
        True/False
        -------------------------------------------------------
        """
#       
        valid = self._is_valid_aux(self._root)
        return valid
    
