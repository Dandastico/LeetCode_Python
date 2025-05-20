'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

# tem um método em Python que se chama str.find() que faz isso tudo
def strStr(haystack, needle):
    return haystack.find(needle)


# vou tentar fazer uma função que faz o que o str.find() faz
def find_idx(haystack, needle):
    length = len(needle)
    err = -1
    
    if length < 1 or length > len(haystack):
        return err
    
    if length == len(haystack) and needle != haystack:
        return err
    
    for i in range(len(haystack)):
        if (length + i) > (len(haystack)):
            return err

        if (length + i) == len(haystack):
            if needle == haystack[i:]:
                return i

        if needle == haystack[i:i+length]:
            return i
        
    return err


print(find_idx("sadbutsad", "sad"))
print(find_idx("leetcode", "leeto"))