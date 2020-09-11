"""
-------------------------------------------------------
[program 1]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-22"
-------------------------------------------------------
"""
from Food_utilities import by_origin, read_foods
from Food import Food


fv = open('foods.txt','r')
print(Food.origins())
origin = int(input("Enter origin:"))
foods = read_foods(fv)
origins = by_origin(foods, origin)

for i in range(len(origins)):
    print(origins[i])

