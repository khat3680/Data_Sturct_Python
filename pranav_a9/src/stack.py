"""
-------------------------
# Student Name: Pranav Verma
# Student ID:193272030
# Student email:verm2030@mylaurier.ca
#-------------------------
"""
from copy import deepcopy


class Stack:
    """
    -------------------------------------------------------
    Implementation of Stack ADT (Array-based Implementation)
    Top of Stack is the last element in the Python list
    -------------------------------------------------------
    """

    def __init__(self):
        """
        -------------------------------------------------------
        Description:
            Initializes a Stack Object
            Initializes items to an empty list
        Use: stack = Stack()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            A Stack object (Stack)            
        -------------------------------------------------------
        """
        self.items = []

    def peek(self):
        """
        -------------------------------------------------------
        Description:
            Returns a copy of top of stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.peek()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            An item from top of stack (?)            
        -------------------------------------------------------
        """
        result = None
        if self.is_empty():
            print("Error(Stack.peek):Invalid peek operation. Stack is empty")
        else:
            result = deepcopy(self.items[-1])
        return result 

    def push(self, item):
        """
        -------------------------------------------------------
        Description:
            Adds an item to the stack
        Use: stack.push(item)
        -------------------------------------------------------
        Parameters:
            item - An item to be added to the stack (?)
        Returns:
            None           
        -------------------------------------------------------
        """
        
        return self.items.append(deepcopy(item))
    
    def pop(self):
        """
        -------------------------------------------------------
        Description:
            Removes the top item of the stack
            if Stack is empty prints error msg and returns None
        Use: item = stack.pop()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            item - An item from top of stack (?)            
        -------------------------------------------------------
        """
        result = None
        if self.is_empty():
            print("Error(Stack.pop):Invalid pop operation. Stack is empty")
        else:
            result = deepcopy(self.items.pop())
        return result
        
    def is_empty(self):
        """
        -------------------------------------------------------
        Description:
            checks if stack is empty
        Use: result = stack.is_empty()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        
        return len(self.items) == 0
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            For testing purposes only, not part of Stack ADT
            Prints all items in stack
            prints [] if stack is empty
        Use: stack.print()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            None
        -------------------------------------------------------
        """
        if self.is_empty():
            output = '[]'
        else:
            output = ''
            for i in range(len(self.items) - 1, -1, -1):
                output = output + str(self.items[i]) + '\n'
        return output


def reverse_str(str1):
    """
    -------------------------------------------------------
    Description:
        Reverse a given string using stacks
    Use: rev_str = reverse_str(input_str)
    -------------------------------------------------------
    Parameters:
        str1 - an input string (str)
    Returns:
        str2 - reversed string (str)
    -------------------------------------------------------
    """
    stack = Stack()
    for char in str1:
        stack.push(char)
    str2 = ''
    while not stack.is_empty():
        str2 += stack.pop()
    return str2


def is_balanced(expression):
    """
    -------------------------------------------------------
    Description:
        Checks if a given expression is balanced
        Uses stacks.
    Use: result = is_balanced(expression)
    -------------------------------------------------------
    Parameters:
        expression - an arbitrary expression (str)
    Returns:
        True/False
    -------------------------------------------------------
    """
    start = ["(", "[", "{"]
    end = [')', ']', '}']
    stack = Stack()
    for char in expression:
        if char in start:
            stack.push(char)
        elif char in end:
            pos = end.index(char)
            if not stack.is_empty() and stack.peek() == start[pos]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True         
    else:
        return False

    
def evaluate_postfix(expression):
    """
    -------------------------------------------------------
    Description:
        Evaluates a postfix expression.
        Uses stacks.
        Expression is formatted such that each term is separated by a space
        Supports seven operators: +,-,*,**,/,// and %
    Use: result = evaluate_postfix(expression)
    -------------------------------------------------------
    Parameters:
        expression - an arbitrary expression (str)
    Returns:
        result - output of expression evaluation (int/float)
    -------------------------------------------------------
    """
    stack = Stack()
    operators = ['**', "*", '%', '/', '//', '+', '-']
    expr_list = expression.split(' ')
    for char in expr_list:
        if char not in operators:
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = calc(operand1, operand2, char)
            stack.push(result)
    return stack.pop()


def calc(operand1, operand2, op):    
    result = None
    if op == "**":
        result = operand1 ** (operand2)
    elif op == "*":
        result = operand1 * operand2
    elif op == '%':
        result = operand1 % operand2
    elif op == '/':
        result = operand1 / operand2
    elif op == '//':
        result = operand1 // operand2
    elif op == '+':
        result = operand1 + operand2
    elif op == '-':
        result = operand1 - operand2
    return result
