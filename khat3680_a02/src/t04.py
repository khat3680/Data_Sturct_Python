"""
-------------------------------------------------------
[program 4]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import read_foods, food_table

fv = open('foods.txt','r')

foods = read_foods(fv)

food_table(foods)
