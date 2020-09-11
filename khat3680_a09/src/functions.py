"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-04-02"
-------------------------------------------------------
"""
from Word import Word

def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in fv and inserts into
    a Hash_Set.
    Each Word object in hash_set contains the number of comparisons
    required to insert that Word object from file_variable into hash_set.
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    lines = fv.read()
    words = lines.split()
    
    for word in words:
        
        if word.isalpha() :
            
            k = Word(word.lower())
            hash_set.insert(k)
    
    return

def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    
    total = 0
    max_word = Word('a')
    
    for word in hash_set:
        
        total += word.comparisons
        
        if word.comparisons > max_word.comparisons :
            
            max_word = word
            
            
    return total , max_word