"""
-------------------------
# Student Name: Pranav Verma
# Student ID:193272030
# Student email:verm2030@gmail.com
#-------------------------
"""

from copy import deepcopy


class Node:
    """
    ----------------------------------------------
    Implementation of a Linked List node
    ----------------------------------------------
    """

    def __init__(self, item, next_node):
        """
        -------------------------------------------------------
        Description:
            Creates and initializes an empty linked list node
            data and next set to given values
        Assert: none
        Use: my_node = Node()
        -------------------------------------------------------
        Parameters:
            item: An arbitrary object (?)
            next_node: reference to another node
        Returns:
            An object of type Node 
        -------------------------------------------------------
        """ 
        self._data = deepcopy(item)
        self._next_node = next_node
        return
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns string representation of node
            Used for testing purposes
        Assert: none
        Use: str(my_node) or print(my_node)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string represenation of node 
        -------------------------------------------------------
        """
        return str(self._data)

    
class Linked_List:
    """
    ----------------------------------------------
    Ordered Indexed Unsorted List
    Linked List Implementation
    ----------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Creates an empty linked list
            head is initialized to None
        Assert: none
        Use: my_list = Linked_list()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type Linked_List       
        -------------------------------------------------------
        """ 
        self._front = None
        self._count = 0
        return
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of linked list
            format: [item1, item2, item3, ...]
        Assert: none
        Use: str(list1) or print(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of linked list (str)
        -------------------------------------------------------
        """
        if self._front is None:
            return '[]'
        output = '['
        current_node = self._front
        while current_node is not None:
            output += str(current_node._data) + ','
            current_node = current_node._next_node
        return output[:-1] + ']'

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for first occurrence
                of the key in the linked list.
            returns key index if found, -1 otherwise
        Assert: none
        Use: p, c, i = self._linear_search(item)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            p: pointer to the node previous to the one containing key (Node)
            c: pointer to the node containing the key (Node) 
            i: index of the node containing key (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._data != key:
            previous = current
            current = current._next_node
            index += 1

        if current is None:
            index = -1
            previous = None

        return previous, current, index
        
    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Description:
            Private helper method to validate an index value
            Valid python list values are -len(list) to len(list)-1
        Assert: i is an integer
        Use: result = self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i: an index value (int)
        Returns:
            result: True if valid index and False otherwise (bool)        
        -------------------------------------------------------
        """
        assert isinstance(i, int), 'invalid i'
        return i < self._count and i >= self._count * -1

    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Check if linked list is empty
        Assert: none
        Use: result = list1.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if list is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Returns number of items in a list
            same as number of nodes
        Assert: none
        Use: length = len(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in the linked list       
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the tail of the linked list
        Assert: none
        Use: my_list.append(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to linked list (?)
        Returns:
            No returns        
        -------------------------------------------------------
        """
        previous = None
        current = self._front

        # Find the last node in the list
        while current is not None:
            previous = current
            current = current._next_node

        # Case 1:linked list is empty
        #    insert into the front of the list
        if previous is None:
            new_node = Node(deepcopy(value), self._front)
            self._front = new_node
        # Case 2: linked list has multiple items
        else:
            new_node = Node(deepcopy(value), current)
            previous._next_node = new_node
        self._count += 1
        return
    
    def reverse(self):
        """
        -------------------------------------------------------
        Description:
           reverses the order of items in linked list
        Assert: no asserts
        Use: list1.reverse()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        new_front = None

        while self._front is not None:
            temp = self._front._next_node
            self._front._next_node = new_front
            new_front = self._front
            self._front = temp

        self._front = new_front
        return
    
    """---------------------- Task 1 ----------------------"""

    def pop(self, i):
        """
        -------------------------------------------------------
        Description:
            Finds, removes and return copy of linked list item at
            position i
            if invalid index or empty list, print error message and
                return None
        Assert: i is an integer
        Use: item = list1.pop(i)
        -------------------------------------------------------
        Parameters:
            i - index of the element to pop (int)
        Returns:
            item: copy of item at position i (?)        
        -------------------------------------------------------
        """
        assert isinstance(i, int), 'invalid i'
        n = 0
        j=0
        if self._is_valid_index(i) is False :
            print("Error(linked_List.pop): invalid i")
            return None
        
        current =self._front
        if i < 0:
                # index is negative
            n = self._count + i
        else:
            n = i
            
        previous = None
        
        while  j < n:

            j += 1
            previous = current
            current = current._next_node
                
                
        self._count -= 1  
        value = current._data   
         
        if previous is None:
            # Remove the first node.
            self._front = self._front._next_node

        else:
            # Remove any other node.
            previous._next_node = current._next_node
    
        
        return value
        

    """---------------------- Task 2 ----------------------"""

    def swap(self, i, j):
        """
        -------------------------------------------------------
        Description:
            swap items at index i with item at index j
            If either i,j is an invalid index, print error message and do nothing
            if i and j are equal do nothing
            if empty list print error message and return
        Assert: i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            i: index of first swapping item (int)
            j: index of second swapping item (int)
        Returns:
            no returns        
        -------------------------------------------------------
        """
        
        assert isinstance(i, int), 'invalid i'
        
        n = 0
        i_1 = 0
        j_1 = 0
        pln  =self._front
        prn =self._front
        
        if self._count == 0:
            print("Error(Linked_List.swap): empty linked list")
            return None
        if self._is_valid_index(i) is False or self._is_valid_index(j) is False:
            print("Error(swap): invalid i or j")
            return None
        if i==j:
            return None
        if self._count == 0:
            print("Error(Linked_List.swap): empty linked list")
            return None
        
        if i < 0:
                # index is negative
            n= i_1 = self._count + i
        else:
            i_1 = i
            
        if j < 0:
                # index is negative
            n= j_1 = self._count + j
        else:
            j_1 = j
            
        
        current = self._front
        
        while current is not None:
            if (i_1 == n):
                pln = current
            if(j_1 == n):
                prn = current
            
            current = current._next_node
            n +=1 
            
        
            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next_node
            else:
                left = pln._next_node
                pln._next = prn._next_node

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next_node
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next_node
            left._next_node = right._next_node
            right._next_node = temp
            # Update the rear
            if right._next_node is None:
                self._rear = right
            elif left._next_node is None:
                self._rear = left
        return
    
    """---------------------- Task 3 ----------------------"""

    def split(self):
        """
        -------------------------------------------------------
        Description:
            Splits list into two parts. 
            listA contains the first half, listB the second half.
            current list becomes empty
        Assert: i and j are integers
        Use: list1.swap(i,j)
        -------------------------------------------------------
        Parameters:
            No input parameters
        Returns:
            listA - a new List with >= 50% of the original List (Linked_List)
            listB - a new List with <= 50% of the original List (Linked_List)
        -------------------------------------------------------
        """
        target1 = Linked_List()
        target2 = Linked_List()
        full = self._count
        half = full // 2
        c = None
        if full % 2 == 0 :
            while c != half:
                target1._move_front_to_rear(self)
                c += 1
            while c != full:
                target2._move_front_to_rear(self)
                c += 1
        else:
            
            while c != (half + 1):
                target1._move_front_to_rear(self)
                c += 1
            c += 1
            while c != (full + 1):
                target2._move_front_to_rear(self)
                c += 1  
            
        return target1, target2

    """---------------------- Task 4 ----------------------"""

    def union(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains all elements that
            appear in either current linked list and given linked list 
            or appear in both linked lists
            items from current list are added before items from list2
            Current and input linked lists are not changed
        Assert: list2 is of type Linked_List
        Use: list3 = list1.union(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of union (Linked_List)
        -------------------------------------------------------
        """
        
        list3 = Linked_List()
        k = 0
        current = self._front
        while current is not None :
            
            _,_,k =list3._linear_search(current._data)
            if k == -1:
                list3.append(current._data)
                
            current = current._next_node
        
        
        current_1 = list2._front
        o = 0
        while current is not None :
            
            _,_,o = list3._linear_search(current_1._data)
            if o == -1 :
                list3.append(current_1._data)
                
            current_1 = current_1._next_node
    
        return list3

    """---------------------- Task 5 ----------------------"""

    def combine(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains all elements that
            contain all items from current list and given list
            duplicates allowed
            Current items are added before list2 items
            Current and list2 become empty
        Assert: list2 is of type Linked_List
        Use: list3 = list1.combine(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of combine (Linked_List)
        -------------------------------------------------------
        """
        
        return
           
    """---------------- Task 6 -------------------------"""

    def intersection(self, list2):
        """
        -------------------------------------------------------
        Description:
            Creates a new linked list that contains only elements that
            appear in both lists, no duplicates
            Current items are added before list2 items
            Current list1 and list2 are not changed
        Assert: list2 is of type Linked_List
        Use: list3 = list1.intersection(list2)
        -------------------------------------------------------
        Parameters:
            list2: an arbitrary linked list (Linked_List)
        Returns:
            list3: a linked list containing result of intersection (Linked_List)
        -------------------------------------------------------
        """
        # your code
        return
