# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

# How Many Numbers Are Smaller Than the Current Number

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))
        
        smaller_counts = {}
       
        for i, (num, original_index) in enumerate(sorted_nums):
            if num not in smaller_counts:
                smaller_counts[num] = i
       
        result = [smaller_counts[num] for num in nums]
        
        return result
