"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
__updated__ = "2020-01-16"
-------------------------------------------------------
"""

from functions import max_diff
a=[]
lent=int(input('Please enter the number of numbers you want to enter'))
for i in range (lent):
    number_s=int(input('Please Enter the number'))
    a.append(number_s)
print("{}".format(max_diff(a)))
