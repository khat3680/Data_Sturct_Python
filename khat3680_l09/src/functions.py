"""
-------------------------------------------------------
[Food keys and the resulting hash values and slots]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-03-18"
-------------------------------------------------------
"""

def hash_table(num_slots, movies):
    """
    ===========================================
    Use:
    ===========================================
    Parameters:
    Movies - list of movie objects
    
    Returns:
    None
    ===========================================
    """
    # print the table header
    print('Hashes\nHash     Slot Key\n======== ==== ====================')
    for i in movies:
        
        h = hash(i)
        slot = h % num_slots
        print("{:8d}{:4d}{:s},{:d}".format(h, slot, i.name, i.origin))
        
    return None
