# 169. majority element
# given an array [nums] of size n, return the majority element
# majority element is the element that appears more than n/2 times.
# you may assume that the majority element always exists in the array

# understand:
#   input: 'nums' array of integers of size n
#   output: majority element integer
# constraints:
#   n == nums.length
#   n at least 1

# approach:
#   iterate through array and generate frequency map of elements.
#   evaluate frequency map for element with majority appearances.

def majorityElement(nums: list[int]) -> int:
    # frequency map of array elements
    freq = {}
    majority = 0
    majorityElement = 0

    for num in nums:
        if num not in freq: freq[num] = 1
        else: freq[num] += 1
    for key in freq:
        if freq[key] > majority:  
            majority = freq[key]
            majorityElement = key
    return majorityElement
# time-complexity: O(N), corresponding to traversal of array and map to determine majority
# space-complexity: O(N), corresponding to frequency hash map 

# boyer-moore majority voting algorithm
def majorityElement2(nums: list[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        # there is either no candidate or count reaches zero, update
        if not candidate or count == 0: 
            candidate = num
            count += 1
        # there is a candidate, but a different element was found
        elif candidate != num: count -= 1
        # there is a candidate, and the same element was found
        else: count +=1
    return candidate
# time-complexity: O(N), corresponding to traverssal of array
# space-complexity: O(1), corresponding to auxiliary data 