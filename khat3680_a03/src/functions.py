"""
-------------------------------------------------------
[Functions for Programs]
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-30"
-------------------------------------------------------
"""


from Stack_array import Stack
from copy import deepcopy

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    i = 1
    while source.is_empty() == False:
        if i == 1:
            target1.push(source.pop())
            i = 2
        elif i == 2:
            target2.push(source.pop())
            i = 1
    
    
    return target1,target2

    
def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    i = 1
    while source1.is_empty()==False or source2.is_empty()==False:
        if i == 1:
            target.push(source1.pop())
            if source2.is_empty() == False:
                i = 2
        elif i == 2:
            target.push(source2.pop())
            if source1.is_empty() == False:
                i = 1
    return target

    
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = None
    newstr = ""
    s = Stack()
    for i in string:
        if i.isalnum():
            newstr += i
    for j in newstr:
        s.push(j)
    revstr = ""
    for k in s:
        revstr += s.pop()
    if revstr.lower() == newstr.lower():
        palindrome = True
    else:
        palindrome = False
        
    return palindrome


# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    ss = string.split()
    for i in ss:
        if i.isdigit():
            s.push(i)
        elif i in OPERATORS:
            val1 = s.pop()
            val2 = s.pop()
            if i == "+":
                s.push(float(int(val2) + int(val1)))
            elif i == "-":
                s.push(float(int(val2) - int(val1)))
            elif i == "*":
                s.push(float(int(val2) * int(val1)))
            elif i == "/":
                s.push(float(int(val2) / int(val1)))
            
    answer = s.pop()
    return answer

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    s = Stack()
    wrongpath = []
    value = maze['Start']
    exfi = False
    
    for i in maze:
        if 'X' in maze[i]:
            path = []
            exfi = False
        elif exfi != False:
            path = None
    if path != None:
        for i in value:
            s.push(i)
            value = s.pop()
            path.append(value)
    while value != 'X' and path != None:
        value = maze[value]
        
        while len(value) == 0:
            value = s.pop()
            
        for i in value:
            if i in path:
                _index = path.index(i)
                wrongpath = path[_index + 1:]
                path = path[:_index]
                
            s.push(i)
        value = s.pop()
        
        path.append(value)
    
        if value in wrongpath:
            value = s.pop()
    return path
