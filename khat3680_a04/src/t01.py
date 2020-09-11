"""
-------------------------------------------------------
[program t01]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-06"
-------------------------------------------------------
"""

from Queue_circular import Queue
from Food_utilities import read_foods

c_queue = Queue()
fv = open("foods.txt",'r')
foods = read_foods(fv)
print(c_queue.is_empty())
for p in foods:
    c_queue.insert(p)
print(c_queue.is_full())
for k in c_queue:
    print(k)
    print("---")

print("Peek---")
print(c_queue.peek())
print()
print("Remove")
print(c_queue.remove())

for j in c_queue:
    print(j)
    print("---")
