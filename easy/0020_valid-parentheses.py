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
        '(': ')',
        '[': ']',
        '{': '}'
        }
    valid = False

    if len(s) % 2 != 0:
        return valid

    for i in range(len(s)-1):
        if s[i] in brackets:
            for j in range(i+1, len(s)):
                if s[j] == brackets[s[i]]:
                    if len(s[i:j+1]) % 2 != 0:
                        return False
                    valid = True
                    break
                else:
                    valid = False

    return valid
                        

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]")) # precisa retonar False porque o colchete não fecha dentro do parênteses
print(isValid("(){}}{")) # retornar False por causa da última chave