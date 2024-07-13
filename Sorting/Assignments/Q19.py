# https://leetcode.com/problems/missing-number/description/

# Missing Number



from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Calculate the expected sum
        expected_sum = n * (n + 1) // 2
        
        # Calculate the actual sum
        actual_sum = sum(nums)
        
        # The missing number is the difference
        missing_number = expected_sum - actual_sum
        
        return missing_number

