from typing import List

def cyclic_Sort(nums: List[int]) -> List[int]:
    i = 0
    N = len(nums)
    while i < N:
        correct = nums[i] - 1
        
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    return nums

nums = [5, 4, 6, 3, 1, 2]
sorted_arr = cyclic_Sort(nums)
print(sorted_arr)
