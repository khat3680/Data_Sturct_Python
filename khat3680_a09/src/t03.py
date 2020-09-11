"""
-------------------------------------------------------
t03
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-04-03"
-------------------------------------------------------
"""
from functions import insert_words,comparison_total
from Hash_Set_array import Hash_Set


fv = open('miserables.txt','r')

hash_1 = Hash_Set(20)

insert_words(fv, hash_1)

total , max_word = comparison_total(hash_1)

print("Using  BST Hash_Set")

print("Total Comparisons: {} ".format(total))

print("Word with maximum comparisons '{}': {}".format(max_word.word,max_word.comparisons))
