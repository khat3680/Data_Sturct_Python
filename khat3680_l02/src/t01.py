"""
-------------------------------------------------------
[program 1]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-20"
-------------------------------------------------------
"""
#from Food import Food
from utilities import stack_test
from Food_utilities import read_foods
list_=[]
k=open('foods.txt','r')
g=read_foods(k)
stack_test(g)