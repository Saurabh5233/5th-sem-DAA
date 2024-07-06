from typing import List
def selection_sort(nums:List[int])-> List[int]:
    N = len(nums)
    for i in range(0,N):
        min = i
        for j in range(i+1,N):
            if nums[j] < nums[min]:
                min = j
        nums[i],nums[min] = nums[min], nums[i]
    return nums

nums = [5,4,6,3,7,2]
sorted_arr = selection_sort(nums)
print(sorted_arr)

# Its not a stable algorithm.......