# 704. binary search
# given an array of integers 'nums' which is sorted in ascending order, and an integer 'target'.
# write a function to search target in nums. if target exists, then return its index. otherwise,
# return -1.
# you must write an algorithm with O(log(n)) runtime complexity.

# understand:
#   input: 'nums' array of integers, 'target' integer
#   output: index of target if it exists, -1 if target does not exist
# constraints:
#   nums array length of at least 1
#   unique integers
#   nums sorted in ascending order

# approach:
#   - take first and last elements and check if target exists in between them
#   - take first and last elements and find median of array
#   - recurse left/right half of array depending on target element until target found or not exist

def binarySearch(nums: list[int], target: int) -> int:
    # initialize traversal pointers
    first, last = 0, len(nums)-1
    # target out-of-bounds condition
    if target < nums[first] and target > nums[last]: return -1

    while first <= last:
        mid = (first+last) // 2
        if nums[mid] > target: last = mid-1
        elif nums[mid] < target: first = mid+1
        else: return mid
    return -1
# time-complexity = O(logN), corresponding to list size reduced based on middle index and target
# space-complexity = O(1)

nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch (nums, target))