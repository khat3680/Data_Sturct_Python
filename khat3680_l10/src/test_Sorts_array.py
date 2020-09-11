"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca  
Section: CP164 Winter 2020
__updated__ = "2020-04-01"
-------------------------------------------------------
"""

# Imports
import random
from Number import Number
from Sorts_array import Sorts


# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    
    values = []
    
    for i in range(SIZE):
        numb = Number(i)
        values.append(numb)
        
        
    
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    
    values = []
    
    for i in range(SIZE-1,-1,-1):
        values.append(Number(i))
        
    return values
    

def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TEST rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    arrays = [ ]
    list_1 = arrays
    
    for i in range(TESTS):
        row = [ ]
        for j in range((SIZE)):
            
            row.append(Number(random.randint(0,XRANGE)))
            
        arrays.append(row)
        
    arrays = list_1
    
    
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    
    a_1 = create_sorted()
    Sorts.swaps = 0  
    func(a_1) 
    swapa = Sorts.swaps
    compa=a_1[0].comparisons
    
    
    
    a_2 = create_reversed()
    Sorts.swaps = 0
    func(a_2)
    swapb = Sorts.swaps
    compb=a_2[0].comparisons
    
    
    a_3 = create_randoms()
    total = 0
    Sorts.swaps = 0
    func(a_3)
    swapc = Sorts.swaps
    for j in a_3:
        total+=j[0].comparisons
        
    compc = total/len(a_3)
    
    print("{:<14} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f}".format(title, compa,compb,compc,swapa,swapb,swapc))
    
    return

for num in SORTS:
    test_sort(num[0],num[1])