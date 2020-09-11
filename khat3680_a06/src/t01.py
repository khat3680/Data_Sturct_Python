"""
-------------------------------------------------------------
[T01]
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
from List_linked import List

l1 = List()
l2 = List()


print("Identical:",l1.is_identical(l2))
print("----------")
print()

fv = open("food.txt",'r')
foods = read_foods(fv)
fv2 = open("food2.txt",'r')
foods2 = read_foods(fv2)

for a in range(len(foods)):
    l1.insert(a, foods[a])
for a in range(len(foods2)):
    l2.insert(a, foods2[a])

for a in l1:
    print(a)
print("----------")
print()

l1.remove_many(foods[0])
print("***Lasagna Removed***")
for a in l1:
    print(a)
    
print("----------")
print()

f = l1.__getitem__(1)
print("***Getting 2nd Item***")
print(f)
print("----------")
print()

l1.clean()
print("***List Cleaned***")
for a in l1:
    print(a)
print("----------")
print()

inter = List()
inter.intersection(l1, l2)
print("***Intersection***")
for a in inter:
    print(a)
print("----------")
print()

union = List()
union.union(l1, l2)
print("***Union***")
for a in union:
    print(a)
print("----------")
print()
    
item = Food("Chaat",2,True,270)
l1.prepend(item)
print("***Item Prepended***")
for j in l1:
    print(j)
print("---------")
print()
   
l2.append(item)
print("***Item appended***")
for j in l2:
    print(j)
print("---------")
print()

value =l2.remove_front()
print("***Front removed***")
print(value)
print("---------")
print()

com = List()
com.combine(l1, l2)
print("***Combined***")
for j in com:
    print(j)
print("---------")
print()   

l1, l2 = com.split()
print("***Split***")
for j in l1:
    print(j)
print()
for j in l2:
    print(j)
print("---------")
print()   

l1 = List()
l2 = List()
for j in range(len(foods)):
    l1.insert(j, foods[j])
for k in range(len(foods2)):
    l2.insert(k, foods2[k])
com.combine(l1, l2)

l1,l2 = com.split_alt()
print("*****Split Alt*****")
for i in l1:
    print(i)
print()
for i in l2:
    print(i)





