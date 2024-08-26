# 268. missing number
# given an array 'nums' containing n distinct numbers in the range [0, n], return the only number in the
# range that is missing from the array

# understand:
#   input: 'nums' array of integers
#       'n' unique numbers
#   output: integer number in the range that is missing from the array

# approach:
#   take range [0, n] and take sum of all elements in the range
#   take sum of all elements in the array
#   return abs of difference

def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expectedSum = 0
    actualSum = 0

    for num in range(0, n+1):
        expectedSum += num

    for num in nums:
        actualSum += num

    return expectedSum - actualSum



nums = [0, 1, 3]
print(missingNumber(nums))