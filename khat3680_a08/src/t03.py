"""
-------------------------------------------------------
[program 3]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-27"
-------------------------------------------------------
"""

from functions import letter_table, do_comparisons
from Letter import Letter
from BST_linked import BST

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

fv = open("miserables.txt","r")
bst1 = BST()
for letter in DATA3:
    ob = Letter(letter)
    bst1.insert(ob)
    
do_comparisons(fv, bst1)

letter_table(bst1)