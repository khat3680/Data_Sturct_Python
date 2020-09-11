"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-11"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods,food_table
def low_cal(foods, count):
    """
    -------------------------------------------------------
    Returns a list of foods with a calorie count less than count.
    Use: low_cal_foods = low_cal(foods, count)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        count - foods must have calories below count (int)
    Returns:
        returns
        low_cal_foods - a list of Food (list of Food)
    -------------------------------------------------------
    """
    low_cal_foods=[ ]
    foods=Food('Shai',2,True,1500)
    if foods.calories < count :
        low_cal_foods=foods #+ low_cal_foods
    return low_cal_foods


fv = open('foods.txt','r')
print(Food.origins())

foods = read_foods(fv)
food_table(foods)

print(low_cal(foods,500))
