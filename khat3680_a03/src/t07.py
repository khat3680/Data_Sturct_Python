"""
-------------------------------------------------------
[program 7]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-30"
-------------------------------------------------------
"""

from functions import stack_maze

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
            'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}

way = stack_maze(maze)

print("Path: {}",format(way)