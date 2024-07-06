from typing import List

# def Q_Sort(nums: List[int], low: int, high: int) -> List[int]:
#     if low < high:
#         partition = func(nums, low, high)
        
#         Q_Sort(nums, low, partition - 1)
#         Q_Sort(nums, partition + 1, high)

#     return nums

# def func(nums: List[int], low: int, high: int) -> int:
#     pivot = nums[low]
#     i = low + 1
#     j = high
    
#     while True:
#         while i <= j and nums[i] <= pivot:
#             i += 1
#         while i <= j and nums[j] >= pivot:
#             j -= 1
#         if i <= j:
#             nums[i], nums[j] = nums[j], nums[i]
#         else:
#             break
    
#     nums[low], nums[j] = nums[j], nums[low]
#     return j
def get_pivot_idx(nums: List[int], low: int, high: int, choice: int = 3) -> int|None:
    match choice:
        case 1:
            return low
        case 2:
            return high
        case 3:
            mid = low + (high - low) // 2
            return mid
        case 4:
            mid = low + (high - low) // 2
            a, b, c = nums[low], nums[mid], nums[high]
            
            if (a <= b <= c) or (c <= b <= a):
                return mid
            elif (b <= a <= c) or (c <= a <= b):
                return low
            else:
                return high
        case _:
            return None
    
    
def Q_Sort(nums:List[int],low:int,high:int)->List[int]:
    if low >= high:
        return 
    
    start = low
    end = high
    # mid = low+(high-low)//2
    pivot = get_pivot_idx(nums,low,high,choice = 3)
    # pivot = nums[mid]
    while start <= end:
        while nums[start] < pivot:
            start +=1
        while nums[end]> pivot:
            end -=1
        if start <= end:
            nums[start], nums[end]= nums[end],nums[start]
            start +=1
            end -=1
            
    # After pivot is at a correct position , sort the right and left halves
    Q_Sort(nums,low,end)
    Q_Sort(nums,start,high)  
    return nums
            


nums = [4, 6, 2, 5, 7, 9, 1, 3]
print(Q_Sort(nums, 0, len(nums) - 1))







            
            