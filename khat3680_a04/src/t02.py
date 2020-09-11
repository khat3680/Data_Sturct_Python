"""
-------------------------------------------------------
[program 2]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-02-06"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue
from functions import pq_split_key
source = Priority_Queue()
source.insert(11)
source.insert(22)
source.insert(44)
source.insert(33)
source.insert(66)
source.insert(5)

print(source._values)
target1, target2 = pq_split_key(source, 44)
for j in target1:
    print(j)
print()

for y in target2:
    print(y)