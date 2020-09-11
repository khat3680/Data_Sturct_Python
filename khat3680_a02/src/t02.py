"""
-------------------------------------------------------
[program 2]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from Food_utilities import average_calories


k=open('foods.txt','r')
goo=read_foods(k)
print("{}".format(average_calories(goo)))
