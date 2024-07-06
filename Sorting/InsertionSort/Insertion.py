from typing import List

def insertionSort(nums:List[int])->List[int]:
    N = len(nums)
    for i in range(1,N):
        
        for j in range(i,0,-1):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
            else:
                break
    return nums
        

nums = [5,4,6,3,7,2]
sorted_arr = insertionSort(nums)
print(sorted_arr)

# Useful in arrays  which has partially sorted segments.........
        