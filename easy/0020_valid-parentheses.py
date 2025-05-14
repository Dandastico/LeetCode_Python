'''
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

Example 4:
Input: s = "([])"
Output: true
'''

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    brackets = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    stk = []

    for char in s:
        if char not in brackets:
            stk.append(char)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()
                if popped != brackets[char]:
                    return False
    return not stk
                        

print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
print(isValid("([])")) # True
print(isValid("([)]")) # False porque o colchete não fecha dentro do parênteses
print(isValid("(){}}{")) # False por causa da última chave