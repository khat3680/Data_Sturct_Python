"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-26"
-------------------------------------------------------
"""
 
from copy import deepcopy
import bisect

 
class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        c = False
        i = 0
        while i < (len(self._values)):
            if self._values[i]== key:
                c = True
            i+=1

        return c

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        value = deepcopy(self._values[i])

        return value

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        
        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        low =  0
        high = len(self._values) - 1
        
        while low < high :
            mid  = (high - low)//2 + low 
            
            if self._values[mid] < key :
                low = mid +1 
            else:
                high = mid
                
        if low == high and self._values[low] == key:
            i = low
        else:
            i = -1
        
        return i
            
    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        
        return i in range(-len(self._values), len(self._values) +1)
    #rember

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        i = 1
        while i < len(self._values):
            if self._values[i] == self._values[i-1]:
                self._values.pop(i)
            else:
                i =i + 1 
                
        return 
             

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        while len(source1._values) > 0 and len(source2._values) > 0 :
            
            if source1._values[0] <= source2._values[0]:
                 
                self._values.append(source1._values.pop(0))
            else:
                
                self._values.append(source2._values.pop(0))
            
        while len(source1._values) > 0:
            self._values.append(source1._values.pop(0))
            
        while len(source2._values) > 0:
            self._values.append(source2._values.pop(0))
            
        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List)
        -------------------------------------------------------
        """
        target = Sorted_List()
        
        target =  deepcopy(self._values[:])

        return target

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        number = 0
        
        if key in self._values:
            for i in range(len(self._values)):
                if self._values[i]== key:
                    number +=1
                
        return number

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        for i in range(len(self._values)):
            if self._values[i] == key:
                value = self._values[i]
            else:
                value = None

        return deepcopy(value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        idx = 0 
        if key in self._values:
            while self._values[idx]!= key:
                idx+=1
            i = self._values[idx]
        else:
            i = -1

        return i

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        bisect.insort(self._values,value)

        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        i = 0 
        j = 0 
        while i < len(source1._values) and j < len(source2._values) :
            if  source1._values[i] < source2._values[j]:
                i+=1 
            elif source1._values[i] > source2._values[j] :
                j+=1
            else:
                if len(self._values) == 0 or self._values[-1] != source1._values[i]:
                    self._values.append(deepcopy(source1._values[i]))
            i+=1
            j+=1
                
        return
            

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """

        return len(self._values) == 0

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values appear
        in the same locations in both lists. (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (Sorted_List)
        Returns:
            identical - True if source contains the same values as target
                in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        identical = False
        if len(target) == len(self._values) : 
            i = 0
            while  i  <  len(target) and target[i] == self._values[i]:
                
                i +=1
            
            if i ==len(self._values):
                identical = True

        return identical


    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'
        idx = (len(self._values))-1
        value = self._values[idx]
        return value

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list' 
        value = self._values[0]
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'
        value = deepcopy(self._values[0])

        return value

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise 
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = 0 
        if key in self._values:
            while self._values[i]!= key:
                i+=1
            value = self._values.pop(i)
        else:
            value = None
        
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'

        value = self._values.pop(0)
        
        return value

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        
        
        value = None
        i=0
       
        while i < len(self._values):
            if key == self._values[i]:
                value = self._values.pop(i)
            
            else:
                value = None
            i+= 1   
        return value 
    

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        hlf = len(self._values)//2 + len(self._values)%2
        
        target1 = self._values[:hlf]
        target2 = self._values[hlf:]
        self._values = []
    
        return target1,target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        Order of target1 and target2 is not significant.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        even = True
        while len(self._values)>0:
            if even:
                a = self._values.pop(0)
                target1.insert(a)
            else:
                b = self._values.pop(0)
                target2.insert(b)
            even = not even

        return target1,target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        
        while len(self._values)>0:
            if func:
                a = self._values.pop(0)
                target1.insert(a)
            else:
                b = self._values.pop(0)
                target2.insert(b)
            

        return target1,target2

        

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List() # all values < key
        target2 = Sorted_List() # all values > key
        if len(self._values) > 0:
            if key < self._values[0]:
                target2._values = self._values
            elif key > self._values[-1] :
                target1._values = self._values
            else:
                i = self._binary_search(key)
                 
                if i == -1 :
                    i = 0 
                    while key > self._values[i]:
                    
                        i += 1
                    target1._values = self._values[:i]
                    target2._values = self._values[i:]
                    
        return target1,target2

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        target = Sorted_List()
        
        for i in source1._values:
            if i not in target:
                target.insert(i)
        for j in source2._values:
            if j not in target:
                target.insert(j)
    
        
        for n in target:
            print(n)

        return

