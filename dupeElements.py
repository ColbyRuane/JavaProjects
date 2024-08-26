# delete duplicate elements from array
def delete_dupes(nums: list[int]) -> list[int]:
    if not nums:
        return nums
    
    pointer = 0
    while pointer < len(nums)-1:
        if nums[pointer] == nums[pointer + 1]:
            nums.pop(nums[pointer+1])
        else:
            pointer += 1
    return nums


# nums = [0, 1, 1, 2, 2, 3, 4, 4, 4, 5]
nums = [-1,0,0,0,0,3,3]
delete_dupes(nums)
print(nums)