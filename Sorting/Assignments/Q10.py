

from typing import List

def targetIndices(nums: List[int], target: int) -> List[int]:
        #  Sort the array
        sorted_nums = sorted(nums)
        
        #  Find the indices of the target value
        target_indices = []
        for i, num in enumerate(sorted_nums):
            if num == target:
                target_indices.append(i)
        
        return target_indices
    
    
nums = [1, 2, 5, 2, 3] 
target = 2
print(targetIndices(nums,target))