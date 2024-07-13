# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

# Find All Duplicates in an Array



from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  # Calculate the index
            
            if nums[index] < 0:
                # If it's negative, the number has been seen before
                duplicates.append(index + 1)
            else:
                # Mark the number as seen by negating it
                nums[index] = -nums[index]
        
        return duplicates

