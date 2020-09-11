"""
-------------------------------------------------------
program
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-12"
-------------------------------------------------------
"""
from Queue_linked import Queue
source = Queue()
source_2 = Queue()
source_3 = Queue()
target = Queue()
t = Queue()
t2 = Queue()


source.insert(11)
source.insert(22)
source.insert(33)
source.insert(1)


source_2.insert(59)
source_2.insert(69)
source_2.insert(77)


source_3.insert(1)
source_3.insert(3)
source_3.insert(2)
#source_3.insert(47)
print("combined vals")
target.combine(source, source_2)

for i in target:
    print(i)
t,t2= source_3.split_alt()

print('val in t')
for i in t:
    print(i)
print("val in t2")
for j in t2:
    print(j)