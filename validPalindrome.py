# 125. valid palindrome

# a phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forwards and backwards
# given a string s, return true if it is a palindrome. otherwise, return false

# understand:
#   input: 's' string, list of characters
#   output: boolean true or false
# constraints:
#   length of 's' at least 1 (length edge-case)
#   s consists of only printable ascii

# approach:
#   1. take string and remove non-alphanumeric characters. uppercase to lowercase

def convertString(input: str) -> str:
    result = []
    for char in input:
        # check for valid char
        if char.isalnum(): result.append(char.lower())
    return ''.join(result)
# python string replace method has complexity of O(N)
# optimized by not replacing each char in a string in worst case

def validPalindrome(s: str) -> bool:
    # empty string edge-case
    if s == '': return True
    # single letter edge-case
    if len(s) == 1: return True

    # remove non-alphanumeric chars and upper -> lower
    s = convertString(s)

    # build stack of s chars
    stack = []
    for char in s:
        stack.append(char)

    for char in s:
        if stack.pop() != char:
            return False
    return True

def validPalindrome2(s:str) -> bool:
    # remove non-alphanumeric chars and upper -> lower
    s = convertString(s)
    length = len(s)

    # single letter edge-case
    if length == 1: return True
    # empty string edge-case
    if s == '': return True

    # pointers for forwards and reverse traversal of string
    left = 0
    right = length-1
    # half-way traversal of string with even-length string boundary
    while left < right or left == right:
        if s[left] != s[right]: return False
        left += 1
        right -= 1
    return True
# time complexity O(N^2), dominated by the python replace method within a for loop
# space complexity O(N) - given that python strings are immutable, replace method creates new strings

# build test case
string = 'racecar'
# string = "A man, a plan, a canal: Panama"
print(validPalindrome2(string))
