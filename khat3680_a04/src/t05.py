"""
-------------------------------------------------------
[program 5]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-06"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

source = Priority_Queue()
source.insert(15)
source.insert(85)
source.insert(35)
source.insert(25)
source.insert(45)
source.insert(65)
source.insert(55)
print(source._values)
t_1,t_2 = source.split_alt()
print(t_1._values)
print(t_2._values)