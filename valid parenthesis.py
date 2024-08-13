"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

input: s = "({[]})"
out: true

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


"""

"""
corner cases: s can't be empty, singleton string

first pass idea: use a stack, push left ones onto stacks, when you reach a right bracket, pop the corresponding stack,
if you try to pop and the stack is empty, return false, if the stack isn't empty at the end, return false, 
if you pop the stack and the chars aren't the same type return false, otherwise return true

def parens(s):
    create new empty stack myStack

    if |s| < 2:
        return false

    for c in s:
        if c == '(' or '[' or '{':
            myStack.push(c)
        else:                       // one of the right brackets
            if myStack is empty:
                return false
            else:
                left = myStack.top
                if left doesn't match c:
                    return false
                else:
                    myStack.pop()
    if myStack is not empty:
        return false
    else:
        return true
            
"""

def parens(s):
    myStack = []

    if len(s) < 2:
        return False
    
    for c in s:
        if c == "(" or c == "[" or c == "{":
            myStack.append(c)
        else:
            if len(myStack) == 0:
                return False
            else:
                left = myStack[-1]
                if left == '(':
                    if c != ')':
                        return False
                elif left == '[':
                    if c != ']':
                        return False
                else:
                    if c != '}':
                        return False
                myStack.pop()

    if len(myStack) > 0:
        return False
    else:
        return True
    
s = "(]"

print(parens(s))
                    