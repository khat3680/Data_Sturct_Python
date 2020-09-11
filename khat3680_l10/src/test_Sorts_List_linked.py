"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-04-02"
-------------------------------------------------------
"""

# Imports
import random
from random import randint

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

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
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = List()
    for i in range(SIZE):
        num = Number(i)
        values.append(num)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    values = List()
    for i in range(SIZE):
        num = Number(i)
        values.prepend(num)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    lists = List()
    
    for x in range(TESTS):
        row = []
        for i in range(SIZE):
            
            v = randint(0,XRANGE)
            num = Number(v) 
            row.append(num)
            
        lists.append(row)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    a = create_sorted()
    Sorts.swaps = 0  
    func(a) 
    swapa = Sorts.swaps
    compa=a[0].comparisons
    
    
    b = create_reversed()
    Sorts.swaps = 0
    func(b)
    swapb = Sorts.swaps
    compb=b[0].comparisons
    
    
    c = create_randoms()
    total = 0
    Sorts.swaps = 0
    func(c)
    swapc = Sorts.swaps
    
    for j in c:
        total+=j[0].comparisons
    compc = total/c._count
    print("{:<14} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f} {:>8.0f}".format(title, compa,compb,compc,swapa,swapb,swapc))
    
    return

