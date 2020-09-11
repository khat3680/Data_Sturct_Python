"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-22"
-------------------------------------------------------
"""

from Hash_Set_array import Hash_Set
hash_set = Hash_Set(7)
hash_set.insert(12)
hash_set.insert(13)
hash_set.insert(14)
hash_set.insert(44)
hash_set.insert(15)

print("Hash set post inserting")
for i in hash_set:
    print(i)
    
    
hash_set.remove(33)
print()
print("Post removing")

for k in hash_set:
    print(k)