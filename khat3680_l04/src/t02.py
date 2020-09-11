"""
-------------------------------------------------------
[program 2]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-05"
-------------------------------------------------------
"""
from utilities import list_test
from Food_utilities import read_foods

fv_ = open('foods.txt','r')
source = read_foods(fv_)
list_test(source)
