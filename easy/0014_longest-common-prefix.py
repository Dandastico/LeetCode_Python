'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs = sorted(strs, key=len)
    smaller = strs[0]
    length = len(smaller)
    found_prefix = False

    for _ in range(len(smaller)):
        if all(s.startswith(smaller[:length]) for s in strs):
            found_prefix = True
        else:
            length -= 1
    
    if found_prefix:
        return smaller[:length]
    else:
        return ""
    

        

    


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))