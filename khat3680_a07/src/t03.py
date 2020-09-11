"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-13"
-------------------------------------------------------
"""

from Deque_linked import Deque
source = Deque()
source_2 = Deque()
source_3 = Deque()
target = Deque()
t = Deque()
t2 = Deque()


source.insert_rear(1)
source.insert_rear(2)
source.insert_rear(3)
source.insert_rear(40)

source_2.insert_rear(59)
source_2.insert_rear(69)
source_2.insert_rear(77)
source_2.insert_rear(80)

source_3.insert_rear(1)
source_3.insert_rear(2)
source_3.insert_rear(2)
source_3.insert_rear(47)


print('val in t')
for i in t:
    print(i)
print("val in t2")
for j in t2:
    print(j)