# 136. single number
# given a non-empty array of integers 'nums', every element appear twice except for one. find it.
# must implement a solution with a linear runtime complexity and use only constant extra space

# understand:
#   input: 'nums' array of integers
#   output: integer array element that appears only once
# constraints:
#   - nums length at least one, non-zero

# approach:
#   XOR operator, !A B or A !B - different elements

def singleNumber(nums):
    # single element edge-case
    if len(nums) == 1: return nums[0]

    result = 0
    for num in nums:
        result ^= num
    # XOR exclusive-or bitwise operator. all elements with 2 instances will evaluate to 0.
    return result    
