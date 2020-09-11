"""
-------------------------------------------------------
[program 8]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
__updated__ = "2020-01-14"
-------------------------------------------------------
"""
from functions import file_analyze
fv=open("numbers.txt", "r+",encoding="utf-8")
print("{}".format(file_analyze(fv)))