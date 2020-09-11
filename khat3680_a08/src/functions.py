"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-25"
-------------------------------------------------------
"""
from Letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    
    line = file_variable.read()
    current = bst._root
     
    for i in line:
        
        if i.isalpha():
            
            i = Letter(i.upper())
            
            while current is not None and current._value!=i:
                
                if current._value > i:
                    current = current._left
                    
                elif current._value < i:
                    current = current._right
                    
            current = bst._root 
    
    return
    
    
    
def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0 
    
    k = bst.inorder()
    
    for j in k:
        
        total += j.comparisons 
    
    return total
    
    


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total_c = 0 
    
    order = bst.inorder()
    
    for obj in order:
        total_c += obj.count 
        
    print("Letter Count/Percent Table")
    print()
    print("Total Count: {:,}".format(total_c))
    print()
    print("Letter  Count       %")
    print("---------------------")
    
    for obj in order:
        
        percent = obj.count * 100 / total_c
        print("{:>5}{:>8,}{:>7.2f}%".format(obj.letter, obj.count, percent))
        
        
    return 