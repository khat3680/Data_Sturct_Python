"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-05"
-------------------------------------------------------
"""


from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_ListNode)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0 


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            value inserted at its sorted position within the sorted list.
        -------------------------------------------------------
        """
        curr = self._front
        prev = None
        
        node = _SL_Node(value,None)
        if self._front is None:

            self._rear = node
            self._front = node
            
        
        elif value > self._rear._value:
            node = _SL_Node(value,None)
            self._rear._next = node
            self._rear = node
            
            
        elif value<self._front._value:
            self._front = _SL_Node(value, self._front) 
            
            
        else:
            
            while curr is not None and node._value>curr._value :
                
                prev = curr   
                curr = curr._next  
                     
            node._next= curr
            prev._next = node
            
            
        self._count+=1   
        
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            curr - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        previous = None
        curr = self._front
        index = 0
        
        while curr is not None and curr._value!=key:
            previous = curr
            curr = curr._next
            index+=1
        if curr is None:
            index = -1
            
        return previous, curr, index


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        previous, curr, index = self._linear_search(key)
        
        if index ==-1:
            value = None
            
        else:
            value = curr._value
            #if it is the first node (curr is equal to front)
            if previous is None:
                self._front = curr._next
                #if you removed the last Node
                if curr._next is None:
                    self._rear = curr._next
                    
            else:
                #remove node somewhere in the middle (or could be the last node)
                previous._next = curr._next
                #if curr was the rear (was pointing to None)
                if curr._next is None:
                    self._rear = previous
            self._count-=1
        return deepcopy(value)

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"


        value = self._front._value
        self._front = self._front._next
        self._count-=1
        if self._count==0:
            self._rear = None
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """

        previous,current,_  = self._linear_search(key)
        
        count = 0
        while current is not None and current._values == key:
            current += current._next
            count +=1
            
        if self._count == count:
            self._front = None
            self._rear = None
            self._count = 0
        elif count > 0: 
            if previous is None:
                self._front = current 
            else:
                previous._next = current
            if current is None:
                self._rear = previous
                
        return 
            
              


    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        _ , curr, index = self._linear_search(key)
        
        if index != -1 :
            value = deepcopy(curr._values)
            
        return value
     
    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        return deepcopy(self._front._values)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        
        _, _, index = self._linear_search(key)
        return index

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """

        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        if i < 0:
            i = self._count +i
        
        j = 0
        curr = self._front
        while j < i :
            curr = curr._next
            j +=1 
        return curr._value
    
    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        return self._linear_search(key) !=-1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        value = self._rear._value

        return deepcopy(value)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        value = self._front._value

        return deepcopy(value)

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """

        _,_,i = self._linear_search(key)
        if i > -1:
            number = 0
            curr = self._front
            while curr is not None and curr._values == key:
                
                curr = curr._next
                number+=1
                
        return number       

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        key_node = self._front
        
        while key_node is not None:
            curr =  key_node._next
            
            while curr is not None and key_node._value == curr._value:
                key_node._next = curr._next
                curr  = curr._next
                self._count -=1
                
            if curr is None:
                self._rear = key_node
                
            key_node  =key_node._next
            
        return
    def pop(self, *i):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(i) <= 1, "No more than 1 argument allowed"

        previous = None
        curr = self._front

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                i[0] = self._count + i[0]
            j = 0

            while j < i[0]:
                previous = curr
                curr = curr._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = curr
                curr = curr._next
                j += 1

        value = curr._value

        if previous is None:
            # Update the front
            self._front = curr._next
        else:
            # Update any other node
            previous._next = curr._next
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the curr list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        
        source1_node = source1._front
        source2_node = source2._front
        
        if source1_node is None and source2_node is None:
            None
        elif source1_node is not None and source2_node is None:
            
            if self._front is None:
                # Add new node to self
                self._front = _SL_Node(source1_node._value, None)
                self._rear = self._front
                self._count += 1
            elif self._rear._value < source1_node._value:
                # Add new node to the end of self
                self._rear._next = _SL_Node(source1_node._value, None)
                self._rear = self._rear._next
                self._count += 1
            else:
                # Value already in self - move to next node in both sources
                source1_node = source1_node._next
                    
                
                
                
            
        elif source1_node is  None and source2_node is not None:
            
            
            
        else:
        
            while source1_node is not None:
                value = source1_node._value
                _, current, _ = source2._linear_search(value)
    
                if current is not None:
                    # Value exists in both source lists.
                    _, current, _ = self._linear_search(value)
    
                    if current is None:
                        # Value does not appear in target list.
                        new_node = _SL_Node(value,None)
            
                        if self._front==None:
                            self._front = new_node
                        if self._rear !=None:
                            self._rear._next = new_node
                        self._rear = new_node
                        self._count+=1
    
                source1_node = source1_node._next
        return
    
    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the curr list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        source_1_node = source1._front

        while source_1_node is not None:
            value = source_1_node._value
            _, curr, _ = self._linear_search(value)

            if curr is None:
                # Value does not exist in new list.
                #self.insert(value)
                new_node = _SL_Node(value,None)
        
                if self._front==None:
                    self._front = new_node
                if self._rear !=None:
                    self._rear._next = new_node
                self._rear = new_node
                self._count+=1
                #insert end
                
            source_1_node = source_1_node._next

        source_2_node = source2._front

        while source_2_node is not None:
            value = source_2_node._value
            _, curr, _ = self._linear_search(value)

            if curr is None:
                # Value does not exist in curr list.
                #self.insert(value)
                new_node = _SL_Node(value,None)
        
                if self._front==None:
                    self._front = new_node
                if self._rear !=None:
                    self._rear._next = new_node
                self._rear = new_node
                self._count+=1

            source_2_node = source_2_node._next
        return


    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. curr list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """

        # your code here

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. curr list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        # your code here

        return

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = l.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """

        if self._count != other._count:
            identical = False
        else:
            source_node = self._front
            other_node = other._front

            while source_node is not None and source_node._value == other_node._value:
                source_node = source_node._next
                other_node = other_node._next

            identical = source_node is None
        return identical

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the curr list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the curr target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        


        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            curr - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here

        return

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        # your code here

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here

        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the curr list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the curr list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """

        # your code here

        return

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the curr Sorted_List and rs
            are interlaced into new_list - curr Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """

        # your code here

        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the curr list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here

        return


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next