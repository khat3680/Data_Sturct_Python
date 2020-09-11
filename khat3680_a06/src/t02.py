"""
-------------------------------------------------------------
[program description]
-------------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-05"
-------------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods
from Sorted_List_linked import Sorted_List

list_1 = Sorted_List()
list_2 = Sorted_List()
print("Identical:",list_1.is_identical(list_2))
print("---------")
print()

f_vp = open("food.txt",'r')
foods = read_foods(f_vp)

f_vp2 = open("food2.txt",'r')
foods2 = read_foods(f_vp2)

for i in range(len(foods)):
    list_1.insert(foods[i])
for i in range(len(foods2)):
    list_2.insert(foods2[i])

for t in list_1:
    print(t)
print("---------")
print()

list_1.remove_many(foods[0])
print("***Lasagna Removed***")
for t in list_1:
    print(t)

print("---------")
print()

f = list_1.__getitem__(1)
print("***Getting 2nd Item***")
print(f)
print("---------")
print()

list_1.clean()
print("***List Cleaned***")
for t in list_1:
    print(t)
print("---------")
print()

inter = Sorted_List()
inter.intersection(list_1, list_2)
print("***Intersection***")
for t in inter:
    print(t)
print("---------")
print()

union = Sorted_List()
union.union(list_1, list_2)
print("***Union***")
for t in union:
    print(t)
print("---------")
print()
    

value =list_2.remove_front()
print("***Front removed***")
print(value)
print("---------")
print()










