# 242. valid anagram
# given two strings s and t, return true if t is an anagram of s, and false otherwise
# an anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once

# understand:
#   input: 's' string, 't' string
#   output: boolean true/false
# constraints:
#   string lengths at least 1
#   s and t consist of lowercase english letters

# approach:
#   - iterate through the strings and keep track of the iterations of each letter (hash map?)
#   - after iterating, directly compare maps of each string for key/value consistency
#   - or have one hash map. iterations of one word increment, the other word decrement. check for 0 map

def isAnagram(s:str, t:str) -> bool:
    # different length edge case
    if len(s) != len(t): return False

    smap, tmap = {}, {}
    for char in s:
        if char not in smap: 
            smap[char] = 0
        else: 
            smap[char] += 1
    for char in t:
        if char not in tmap: 
            tmap[char] = 0
        else: 
            tmap[char] += 1

    # different keys failure case
    if smap.keys() != tmap.keys(): return False
    # same keys, check values
    for key in smap.keys():
        if smap[key] != tmap[key]: return False
    return True
# time-complexity: O(N), corresponding to the worst-case scenario of the input strings comprising
#   of unique elements (larger dictionary/hash map size)
# space-complexity: O(N), corresponding to maximum size of the hash maps

s = 'anagram'
t = 'nagrama'
print(isAnagram(s,t))
