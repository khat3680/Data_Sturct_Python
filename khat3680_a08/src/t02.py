"""
-------------------------------------------------------
[program 2]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-25"
-------------------------------------------------------
"""
from BST_linked import BST
from functions import comparison_total , do_comparisons
from Letter import Letter


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

for i in DATA1:
    bst1.insert(Letter(i[0]))


for i in DATA2:
    bst2.insert(Letter(i[0]))
    

for i in DATA3:
    bst3.insert(Letter(i[0]))
    
f_variable = open("miserables.txt","r")


print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
do_comparisons(f_variable, bst1)

total = comparison_total(bst1)
print("Total Comparisons: {:,.0f}".format(total))

print("------------------------------------------------------------")

    
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
do_comparisons(f_variable, bst2)

total = comparison_total(bst2)
print("Total Comparisons: {:,.0f}".format(total))


print("------------------------------------------------------------")


print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
do_comparisons(f_variable, bst3)

total = comparison_total(bst3)
print("Total Comparisons: {:,.0f}".format(total))