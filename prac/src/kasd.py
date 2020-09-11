"""
-------------------------------------------------------
PRACTICE
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-31"
-------------------------------------------------------
"""

from Stack_array import Stack
from copy import deepcopy
"""
#from Sorted_List_array import Sorted_List
from List_array import List

def balanced_brackets(exp):
    
    -------------------------------------------------------
    Determines if an expression has balanced brackets. Tested bracket
    pairs are (), [], {}. Rest of string is ignored.
    -------------------------------------------------------
    Parameters:
        exp - expression to test for balanced brackets (str)
    Returns:
        balanced - True if brackets in exp are balanced,
            False otherwise (boolean)
    -------------------------------------------------------
    
    balanced = False
    s=Stack()
    
    
    if len(exp) == 0:
        balanced = True
    
    elif len(exp)%2 != 0:
        
        balanced = False
        
    else :
        
        for i in range(len(exp)):
            
        
            if exp[i]=="(" or exp[i]=="[" or exp[i]=="{":
        
                s.push(exp[i])
                
        
            elif exp[i] == ")" or exp[i] == "]" or exp[i] == "}" :
                
                print(s._values)
                if s.is_empty() :
                    balanced = False
                else:
                    s.pop()
                    
                    
        if s.is_empty() :
                    balanced = True            
        
    return  balanced  
 

def remove_many(self, key):
    
    ---------------------------------------------------------
    Removes all values that match key in source.
    Use: source.remove_many(key)
    ---------------------------------------------------------
    Parameters:
        key - the key to match (?)
    Returns:
        None
    ---------------------------------------------------------
    
    (For full marks the code must take advantage of the fact the the list is sorted.)"""
    
"""
    self._linear_search(key)
    value = None
    i=0
       
    while i < len(self._values):
        if key == self._values[i]:
            value = self._values.pop(i)
        
        else:
            value = None
        i+= 1   
    return value
"""

def combine(self, source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into the current target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target.combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - an array-based stack (Stack)
        source2 - an array-based stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    
    i = 1
    while source1._values != [] or source2._values != []:
        if i == 1:
            self._values.append(deepcopy(source1._values.pop()))
            if source2._values != []:
                i = 2
        elif i == 2:
            self._values.append(deepcopy(source2._values.pop()))
            if source1._values != []:
                i = 1
                
    return
