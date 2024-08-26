# 1. Two Sum - Easy

# given an array of integers [nums] and an integer [target], return indices of the two numbers
# such that they add up to target

# you may assume that each input would have exactly one solution, and you may not use the same element
# twice. you can return the answer in any order

# constraints: 
#   nums length of at least 2

# understand
#   input: nums array of integers. target integer
#   output: pair of integers (indices), tuple, list of two integers

# brute force algorithm: 
#   nested for-loops. for each index in the array, check every other array element and evaluate whether
#   the two elements have a sum equal to the target
# brute-force time complexity = O(N^2)
#   pair of nested for-loops

def twoSum(nums: list[int], target:int) -> tuple[int, int]:
    length = len(nums)
    # iterate through array indices
    for i in range(length):
        # compare every other element with current array element
        for j in range(length):
            print(f'compare {nums[i]} at index {i} with {nums[j]} at index {j}')
            # do not evaluate the same element twice
            if i != j:
                # return pair of indices if they equal target
                if nums[i] + nums[j] == target:
                    return [i, j]
    return []

# more efficient algorithm: array traversal with hash map
# time-complexity = O(N)
#   in worst-case, single traversal through array. hash map constant lookup

def twoSumTwo(nums: list[int], target: int) -> tuple[int]:
    # empty hash map and grab array length
    length = len(nums)
    map = {}

    # single pass through array
    for index in range(length):
        # check what complement could result in the solution
        pair = target - nums[index]
        # check if complement exists in array
        if pair in map:
            return [index, map[pair]]
        
        # if complement does not exist, store current element in map
        # key is element, value is index
        map[nums[index]] = index
    return []

    

nums = (2, 7, 11, 15) 
target = 9
print(twoSumTwo(nums, target))