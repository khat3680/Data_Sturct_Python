"""
-------------------------------------------------------
[program 5]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import read_foods, food_search


fv = open('foods.txt','r')

origin = int(input("Enter origin:"))
foods = read_foods(fv)
max_cals = int(input("Enter Max calories:"))
is_veg = input("Enter if is veg:")

results = food_search(foods, origin, max_cals, is_veg)
for i in range(len(results)):
    print(results[i])
    print()