"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-22"
-------------------------------------------------------
"""
from functions import hash_table
from Food_utilities import read_foods

f_v = open("foods.txt", "r")

foods = read_foods(f_v)

hash_table(6, foods)