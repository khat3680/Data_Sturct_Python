"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-07-04"
-------------------------------------------------------
"""
from A7 import Linked_List


def test_pop():
    print('{}'.format('-' * 20))
    print('Testing Linked_List.pop:\n')
    
    list1 = Linked_List()
    print('Creating a new linked list with arbitrary items:')
    for i in range(10, 110, 10):
        list1.append(i)
    print('list1 = {}'.format(list1))
    print()
  
    cases = [0, 2, 7, -1, -6, -6, 5]
    for i in cases:
        print('list1.pop({}) = '.format(i), end='')
        item = list1.pop(i)
        print(item)
        print('list1 = {}'.format(list1))
        print()
        
    print('End of Linked_List.pop testing')
    print('{}\n'.format('-' * 20))
    return


def test_swap():
    print('{}'.format('-' * 20))
    print('Testing Linked_List.swap:\n')
    
    print('Create an empty linked list:')
    list1 = Linked_List()
    print('list1 = {}'.format(list1))
    print('swap(0,2):')
    list1.swap(0, 2)
    print()
    
    print('Add item 10 to list:')
    list1.append(10)
    print('list1 = {}'.format(list1))
    print('swap(0,0):')
    list1.swap(0, 0)
    print('list1 = {}'.format(list1))
    print('swap(0,1):')
    list1.swap(0, 1)
    print('list1 = {}'.format(list1))
    print()
    
    print('Add item 20 to list:')
    list1.append(20)
    print('list1 = {}'.format(list1))
    print('swap(1,2):')
    list1.swap(1, 2)
    print('list1 = {}'.format(list1))    
    print('swap(2,2):')
    list1.swap(2, 2)
    print('list1 = {}'.format(list1))
    print()
    
    print('Add 8 more items:')
    for i in range(30, 110, 10):
        list1.append(i)
    print('list1 = {}'.format(list1))
    print()
    
    cases = [[2, 2], [1, 3], [2, 8], [4, 5], [0, 2], [1, 9], [0, 9], [9, 0], [-1, -10], [-2, -9]]
    for case in cases:
        print('swap({},{}):'.format(case[0], case[1]))
        list1.swap(case[0], case[1])
        print('list1 = {}'.format(list1))
        print()

    print('End of Linked_List.swap testing')
    print('{}\n'.format('-' * 20))
    return


def test_setitem():
    print('{}'.format('-' * 20))
    print('Testing Linked_List.__setitem__ :\n')
    
    list1 = Linked_List()
    print('Creating a new linked list with 6 items:')
    for i in range(10, 70, 10):
        list1.insert_front(i)
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print()
  
    list1[0] = 10
  
    cases = [[0, 1], [1, 2], [-1, 6], [-2, 5]]
    for i in range(len(cases)):
        print('list1[{}] = {}'.format(cases[i][0], cases[i][1]))
        list1[cases[i][0]] = cases[i][1]
        print('list1 = {}'.format(list1))
        print()
        
    print('End of Linked_List.__setitem__ testing')
    print('{}\n'.format('-' * 20))
    return


def test_split():
    print('{}'.format('-' * 20))
    print('Testing Linked_List.split :\n')
    
    list1 = Linked_List()
    for i in range(10):
        for j in range(i):
            list1.append(j)
        print('list = {}'.format(list1))
        listA, listB = list1.split()
        print('listA = {}'.format(listA))
        print('listB = {}'.format(listB))
        print('list = {}'.format(list1))

        print()
        
    print('End of Linked_List.split testing')
    print('{}\n'.format('-' * 20))
    return


def test_union():
    print('{}'.format('-' * 20))
    print('Testing Linked_List.union:\n')
    
    list1 = Linked_List()
    list2 = Linked_List()  
    print('list1 = {}'.format(list1))
    print('list2 = {}'.format(list2))
    print('list1.uniont(list2) = {}'.format(list1.union(list2)))
    print()
    
    list1.append(1)
    print('list1 = {}'.format(list1))
    print('list2 = {}'.format(list2))
    print('list1.uniont(list2) = {}'.format(list1.union(list2)))
    print()
    
    list2.append(10)
    print('list1 = {}'.format(list1))
    print('list2 = {}'.format(list2))
    print('list1.uniont(list2) = {}'.format(list1.union(list2)))
    print()
    
    list1.append(1)
    print('list1 = {}'.format(list1))
    print('list2 = {}'.format(list2))
    print('list1.uniont(list2) = {}'.format(list1.union(list2)))
    print()
    
    list2.append(10)
    print('list1 = {}'.format(list1))
    print('list2 = {}'.format(list2))
    print('list1.uniont(list2) = {}'.format(list1.union(list2)))
    print()
    
    list1.append(2)
    list1.append(3)
    list1.append(2)
    list1.append(4)
    list2.append(20)
    list2.append(20)
    list2.append(30)
    print('list1 = {}'.format(list1))
    print('list2 = {}'.format(list2))
    print('list1.uniont(list2) = {}'.format(list1.union(list2)))
    print()
    
    print('End of Linked_List.union testing')
    print('{}\n'.format('-' * 20))
    return


def test_combine():
    print('{}'.format('-' * 20))
    print('Testing Linked_List.combine():\n')
    
    print('Create list1 with arbitrary items')
    list1 = Linked_List()   
    list2 = Linked_List()

    print('Before combine:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    list3 = list1.combine(list2)
    print('After combine:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    print('len(list3) = {} , list3 = {}'.format(len(list3), list3))
    print()

    for i in range(10, 60, 10):
        list1.append(i)
    print('Before combine:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    list3 = list1.combine(list2)
    print('After combine:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    print('len(list3) = {} , list3 = {}'.format(len(list3), list3))
    print()
    
    for i in range(10, 60, 10):
        list1.append(i)
    for i in range(60, 110, 10):
        list2.append(i)
    print('Before combine:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    list3 = list1.combine(list2)
    print('After combine:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    print('len(list3) = {} , list3 = {}'.format(len(list3), list3))
    print()
    
    print('End of Linked_List.combine testing')
    print('{}\n'.format('-' * 20))
    return


def test_intersection():
    print('{}'.format('-' * 20))
    print('Testing Linked_List.intersection():\n')
    
    print('Create list1 with arbitrary items')
    list1 = Linked_List()   
    list2 = Linked_List()

    print('Before interesection:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    list3 = list1.intersection(list2)
    print('After intersection:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    print('len(list3) = {} , list3 = {}'.format(len(list3), list3))
    print()

    for i in range(10, 60, 10):
        list1.append(i)
    print('Before interesection:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    list3 = list1.intersection(list2)
    print('After intersection:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    print('len(list3) = {} , list3 = {}'.format(len(list3), list3))
    print()
    
    for i in range(40, 120, 10):
        list1.append(i)
    for i in range(110, 10, -15):
        list2.append(i)
    print('Before interesection:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    list3 = list1.intersection(list2)
    print('After intersection:')
    print('len(list1) = {} , list1 = {}'.format(len(list1), list1))
    print('len(list2) = {} , list2 = {}'.format(len(list2), list2))
    print('len(list3) = {} , list3 = {}'.format(len(list3), list3))
    print()
    
    print('End of Linked_List.intersection testing')
    print('{}\n'.format('-' * 20))
    return


#test_pop()
#test_swap()
#test_split()
test_union()
# test_combine()
# test_intersection()
