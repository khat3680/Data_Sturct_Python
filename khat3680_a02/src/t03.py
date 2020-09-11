"""
-------------------------------------------------------
[program 3]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import read_foods , calories_by_origin 
from Food import Food


k=open('foods.txt','r')
goo=read_foods(k)
print(Food.origins())
preference=int(input('Enter Origin of Dish (in Number) : '))

print("Average Calories of dishes from Origin: {} is :{}".format(preference,calories_by_origin(goo,preference)))
