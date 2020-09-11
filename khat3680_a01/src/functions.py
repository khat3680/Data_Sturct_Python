"""
Fucntions for programs
-------------------------------------------------------
program description
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Section: CP164 Winter 2020
Email:   khat3680@mylaurier.ca
__updated__ = "2020-01-16"
-------------------------------------------------------
"""

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    md=0
    for i in range(1,len(a)):    
        if  md <= a[i-1]-a[i] or md <= a[i]-a[i-1] :
            md = abs(a[i-1]-a[i])
    return abs(md)

def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid=False
    if name[0].isalpha() or name[0]=='_':
        for i in name:
            
            if i=='_' or i.isdigit() or i.isalpha():
                valid = True 
            else: 
                valid=False
    else:
        valid=False
    return valid
    
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    print(a)
    large=a[0][0]
    small=a[0][0]
    total=0
    average=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] >= large :
                large=a[i][j]
            if a[i][j] <= small :
                small=a[i][j]
                
            total+=a[i][j]
            average=total/(len(a[i]))
    return small, large, total, average/len(a)
    
def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    a must be unchanged.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """ 
    b=[]
    for i in range(len(a)):
        for j in range(len(a[i])):
            b.append(a[i][j])
        
    return b

def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    c=[]
    for i in range(len(a)):
        k=[]
        for j in range(len(a[i])):
            k.append(a[i][j] + b[i][j]) #c[i][j]= a[i][k] * b[k][j]
        c.append(k)
    return c

def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]  
 
  
    for i in range(len(a)):  
        for j in range(len(b[0])):  
            for k in range(len(b)):  
                result[i][j] += a[i][k] * b[k][j]
    return result 

def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b=[]
    i=0
    d=1
    
    while i < d:
        k=[]
        for j in range(len(a)):
            k.append(a[j][i])
        b.append(k)
        d=len(a[i])
        i=i+1
        
    return b

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u= 0
    l=0
    d=0
    w=0
    r=0
    for i in fv:
        if i.isupper() :
            u += 1
        if i.islower() :
            l +=1 
        if i.isdigit() :
            d+= 1
        if i.isspace() : 
            w+=1
        if not i.isupper() and not i.islower() and not i.isdigit() and not i.isspace() :  
            r+=1 
    return u,l,d,w,r
            
def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out=" "
    for i in s:
        if i=='a' or i=='A' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u' :
            None
        else:
            out=out+ i
    
    return out

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """ 
    
    if word[0]=='a' or word[0]=='A' or word[0]=='E' or word[0]=='e' or word[0]=='I' or word[0]=='i' or word[0]=='O' or word[0]=='o' or word[0]=='U' or word[0]=='u' :
        pl=word+"way"
    else:
        pl=word[1:] + word[0]
        for i in range(len(word)):
            if word[i]=='a' or word[i]=='A' or word[i]=='E' or word[i]=='e' or word[i]=='I' or word[i]=='i' or word[i]=='O' or word[i]=='o' or word[i]=='U' or word[i]=='u' or word[i]=='Y' or word[i]=='y' :
                break
            else:
                pl=word[i+1:]+pl[-1]+ word[i]
                print(pl)
        pl=pl+ "ay"        
    if word[0].isupper() :
        pl=pl.lower()
        pl=pl.capitalize()
    return pl
    
       
        
            

    
    
    
    
    
    