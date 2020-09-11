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
        
        value=0
        assert self._is_valid_index(i), "Invalid index value"
        count=-1
        curr=self._front
        while curr is not None and count!=i+1:
            if i <0 :
                i = i + self._count 
            
            if i == count+1 :
                value=deepcopy(curr._value)
            
            count+=1
            curr=curr._next
        return value
        """
        assert self._is_valid_index(i), "Invalid index value"
        
        curr=self._front
        if i < 0: 
            i= self._count + i
        k=0
        while k<i : 
            #new_node = _List_Node(deepcopy(value),None)
            
            curr = curr._next 
            k+=1
        value=deepcopy(curr._value)
        # your code here
        return value
    