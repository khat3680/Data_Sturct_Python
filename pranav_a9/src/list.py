"""
-------------------------
# Student Name: Pranav Verma
# Student ID:193272030
# Student email:verm2030@mylaureier.ca
#-------------------------
"""

from copy import deepcopy


class List:
    """
    ----------------------------------------------
    Ordered Indexed Unsorted List
    Array Implementation
    ----------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Creates an empty list
        Assert: none
        Use: my_list = List()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An object of type List       
        -------------------------------------------------------
        """
        self._items = []

    def __len__(self):
        """
        -------------------------------------------------------
        Description:
            Compute number of items in a list
        Assert: none
        Use: length = len(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            length: number of items in the        
        -------------------------------------------------------
        """
        return len(self._items)
    
    def append(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds given item to the tail of the list
        Assert: none
        Use: list1.append(item)
        -------------------------------------------------------
        Parameters:
            item: an arbitrary item to add to list
        Returns:
            No returns        
        -------------------------------------------------------
        """
        self._items += [deepcopy(item)]

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Description:
            Private helper method to search for first occurrence
                of the key in the list.
            returns key index if found, -1 otherwise
        Assert: none
        Use: indx = self._linear_search(item)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            indx: position of key in the list (int)
        -------------------------------------------------------
        """
        indx = -1
        for i in range(len(self)):
            if self._items[i] == key:
                indx = i
                break
        return indx
        
    def remove(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds, removes, and returns the value in list that matches key.
            if key not found returns None
            If list is empty, prints an error message and returns None
        Assert: none
        Use: item = list1.remove(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(List.remove): Cannot remove from an empty list')
            return None
        i = self._linear_search(key)
        if i == -1:
            item = None
        else:
            item = deepcopy(self._items[i])
            self._items = self._items[:i] + self._items[i + 1:]
        return item

    def find(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds and returns a copy of item in list that matches key.
            If item not found returns None
        Assert: none
        Use: item = list1.remove(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            item: the full item matching key (?)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return deepcopy(self._items[i]) if i != -1 else None
        
    def __iter__(self):
        """
        -------------------------------------------------------
        Description:
            Generates a Python iterator.
            Iterates from item at index 0 to end of list
        Assert: none
        Use: for item in list1:
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            item - the next value in the list (?)
        -------------------------------------------------------
        """
        for item in self._items:
            yield item
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Returns a string representation of list
            format: [item1, item2, item3, ...]
        Assert: none
        Use: str(list1) or print(list1)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            output: string representation of the list (str)
        -------------------------------------------------------
        """
        if self.is_empty():
            return '[]'
        output = '['
        for item in self:
            output += str(item) + ','
        return output[:-1] + ']'

    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            Compute number of items in a list
        Assert: none
        Use: result = list1.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if list is empty, False otherwise (bool) 
        -------------------------------------------------------
        """
        return len(self) == 0
    
    def __contains__(self, key):
        """
        -------------------------------------------------------
        Description:
            Returns True if list contains an item in the list that
                matches given key, returns False otherwise
        Assert: none
        Use: result = key in list1
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            result: True/False
        -------------------------------------------------------
        """
        return self._linear_search(key) != -1
    
    def count(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds the number of times key appears in the list
        Assert: list is not empty
        Use: counter = list1.count(key)
        -------------------------------------------------------
        Parameters:
            key: a partial data element to search for (?)
        Returns:
            result: number of ocurrences of key in the list (int)
        -------------------------------------------------------
        """
        assert len(self) > 0, "Cannot count keys in an empty list"
        counter = 0
        for i in range(len(self)):
            if self._items[i] == key:
                counter += 1
        return counter

    def max(self):
        """
        -------------------------------------------------------
        Description:
            Find maximum value in list
        Assert: list is not empty
        Use: max_item = list1.max()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            max_item: copy of item with maximum value (?)
        -------------------------------------------------------
        """
        assert len(self) > 0, "Cannot find maximum of an empty list"
        max_index = 0
        for i in range(len(self)):
            if self._items[i] > self._items[max_index]:
                max_index = i
        return deepcopy(self._items[max_index])

    def min(self):
        """
        -------------------------------------------------------
        Description:
            Find maximum value in list
        Assert: list is not empty
        Use: min_item = list1.min()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            min_item: copy of item with minimum value (?)
        -------------------------------------------------------
        """
        assert len(self) > 0, "Cannot find minimum of an empty list"
        min_index = 0
        for i in range(len(self)):
            if self._items[i] < self._items[min_index]:
                min_index = i
        return deepcopy(self._items[min_index])
    
    def copy(self):
        """
        -------------------------------------------------------
        Description:
            Returns a duplicate copy of current list
        Assert: no asserts
        Use: list2 = list1.copy()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            new_list: copy or current list (List)
        -------------------------------------------------------
        """
        new_list = List()
        new_list._items = deepcopy(self._items)

        return new_list 

    def clear(self):
        """
        -------------------------------------------------------
        Description:
            removes all items in current List
        Assert: no asserts
        Use: list1.clear()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        for item in self:
            self.remove(item)
        return
    
    def clean(self):
        """
        -------------------------------------------------------
        Description:
            removes all duplicates from the current list
            The first instance is preserved
        Assert: no asserts
        Use: list1.clean()
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        self._items = self._clean_r(self._items)
    
    def _clean_r(self, items):
        """
        -------------------------------------------------------
        Description:
            Private helper method to remove duplicates
            Uses recursion
        Assert: no asserts
        Use: self._clean_r(self._items)
        -------------------------------------------------------
        Parameters:
            No parameters
        Returns:
            No returns
        -------------------------------------------------------
        """
        if len(items) <= 1:
            return items
        if items[-1] in items[:-1]:
            return self._clean_r(items[:-1])
        return self._clean_r(items[:-1]) + [items[-1]]

    def identical(self, list2):
        """
        -------------------------------------------------------
        Description:
            Check if list2 is identical to current list
            Check if items are equal and in same order
        Assert: list2 is a List
        Use: result = list1.identical(list2)
        -------------------------------------------------------
        Parameters:
            list2: a List object to compare to current List (List) 
        Returns:
            True if identical, False otherwise (bool)
        -------------------------------------------------------
        """
        assert isinstance(list2, List), "invalid list2"
        if len(self) != len(list2):
            return False
        for i in range(len(self)):
            if self[i] != list2[i]:
                return False
        return True

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
        assert isinstance(i, int), "invalid i"
        return i < len(self) and i >= len(self) * -1
    
    def index(self, key):
        """
        -------------------------------------------------------
        Description:
            Finds location of a value by key in list.
            Returns the position of the item that match given key
            Returns -1 if not found
        Assert: No asserts
        Use: i = list1.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - location of key in the list (int)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return i

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of the ith element of the list
        Assert: i is an integer and is a valid index
        Use: item = list1[i]
        -------------------------------------------------------
        Parameters:
            i: an index value (int)
        Returns:
            result: copy of ith element in list (?)      
        -------------------------------------------------------
        """
        assert isinstance(i, int) and self._is_valid_index(i), 'invalid index'
        return deepcopy(self._items[i])

    def __setitem__(self, i, item):
        """
        -------------------------------------------------------
        Description:
            Places a copy of value into the list at position i
        Assert: i is a valid index
        Use: list1[i] = item
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            item - an item to be added (?)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        assert isinstance(i, int) and self._is_valid_index(i), 'invalid index'
        self._items[i] = deepcopy(item)
        return

    def insert(self, i, item):
        """
        -------------------------------------------------------
        Description:
            inserts a copy of given item into the list at index i
            If invalid index assert
        Assert: i is an integer
        Use: list1.insert(i,item)
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            item - an item to be added (?)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        assert isinstance(i, int), 'invalid i'
        if self._is_valid_index(i):
            self._items = self._items[:i] + [deepcopy(item)] + self._items[i:]
        else:
            self._items += [deepcopy(item)]
        return

    def delete(self, i):  # different than __del__
        """
        -------------------------------------------------------
        Description:
            removes the item at position i 
        Assert: i is a valid index and current list is not empty
        Use: list1.delete(i)
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            No returns     
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'invalid i'
        assert not self.is_empty(), 'Cannot delete from empty list'
        self._items = self._items[:i] + self._items[i + 1:]
        return

    def pop(self, i):
        """
        -------------------------------------------------------
        Description:
            removes item at position i and return a copy
            If invalid index, print error message and return None
        Assert: no asserts
        Use: list1.pop(i)
        -------------------------------------------------------
        Parameters:
            i - index of the element to pop (int)
        Returns:
            item: copy of item at position i (?)    
        -------------------------------------------------------
        """
        if self.is_empty():
            print('Error(List.pop):List is empty')
            return None
        if not self._is_valid_index(i):
            print('Error(List.pop):Invalid value of i')
            return None
        return self.remove(self[i])
        
