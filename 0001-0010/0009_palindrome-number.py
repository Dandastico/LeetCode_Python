'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Challenge: Solving the problem without converting the int to str
'''


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    
    digits = []
    digits_inv = []

    while x != 0:
        digit = x % 10
        digits.insert(0, digit)
        digits_inv.append(digit)
        print(digits)
        print(digits_inv)
        x = x // 10

    if digits == digits_inv:
        return True

    return False

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
        

