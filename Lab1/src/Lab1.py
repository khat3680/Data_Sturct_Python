"""
-------------------------
# Student Name: 
# Student ID:
# Student email:
#-------------------------
"""


def read_airports(filename):
    """
    -------------------------------------------------------
    Description:
        Reads a file containing airport records. File format:
        (code)-province:airport_name
        The code-name is stored in a dictionary
        list of provinces is stored in a set
    Use: airport_dict,province_set = read_airpors(filename)
    -------------------------------------------------------
    Parameters:
        filename - name of file (str)
    Returns:
        airport_dict - dictionary containing codes & airport names (dict)
        province_set - set of provinces (set)            
    -------------------------------------------------------
    """
    # your code here
    return None,None

def query_airports_DB(code_name_dict,prov_code_dict):
    """
    -------------------------------------------------------
    Description:
        Constructs a dictionary such taht:
            - Key is a province
            - Value is a tuple containing all airport names in that province
        Two dictionaries are given:
            1- Code - airport name
            2- province - string of airport codes separated by a space
    Use: dict3 = query_airports_DB(dict1,dict2)
    -------------------------------------------------------
    Parameters:
        code_name_dict - dictionary of codes-names (dict)
        prov_code_dict - dictionary of provinces-codes (dict)
    Returns:
        prov_name_dict - dictionary of province-names (dict)          
    -------------------------------------------------------
    """
    # your code here
    return None
        
def is_array(data):
    """
    -------------------------------------------------------
    Description:
        Checks if given data is an array.
        An array is: an ordered and mutable data structure
            all elements are of the same type
            if elements are collections, then they all share same size
    Use: result = is_array(data)
    -------------------------------------------------------
    Parameters:
        data - an arbitrary data to be tested (data)
    Returns:
        True if data is an array and False otherwise         
    -------------------------------------------------------
    """
    # your code here
    return False

def get_num_baskets(collection):
    """
    -------------------------------------------------------
    Description:
        Read numbers stored in a collection
        constructs a list containing baskets.
        A basket is a set containing all numbers of equal #digits
        basket0: contains single-digit numbers
        basket1: contains 2-digit numbers
        ...
        If input is not a list,tuple or set, print error and return empty set
    Use: baskets = get_num_baskets(collection)
    -------------------------------------------------------
    Parameters:
        collection - a collection containing numbers (list,tuple,set)
    Returns:
        baskets = list containing sets of numbers (list)
    -------------------------------------------------------
    """
    # your code here
    return None

def is_valid_container(text):
    """
    -------------------------------------------------------
    Description:
        Checks if given string represent a valid python container (list,tuple,set) 
        assume the string contains no spaces
    Use: result = is_valid_container(text)
    -------------------------------------------------------
    Parameters:
        text - a string representing a python container (text)
    Returns:
        True if text is a valid container and Fralse otherwise
    -------------------------------------------------------
    """
    result = True
    
    if isinstance(text,int)  or isinstance(text, float):
        result = None
    
    else:
        
        if len(text) > 1:
            
            if text[0] =='[' :
                
                if text[len(text)-1]=="]":
                     
                    result = True  
                    
             
                 
            if text[0] =='{' :
                 
                if text[len(text)-1]=="}":
                     
                    result =True
                
                     
                 
            if text[0] =='(' :
                 
                if text[len(text)-1]==")":
                     
                    result = True
                 
             
           
             
        
                           
                

    
    return result
