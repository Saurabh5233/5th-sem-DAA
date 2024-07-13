# https://leetcode.com/problems/squares-of-a-sorted-array/

# Squares of a Sorted Array


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrArr =[]
        for i in nums:
            sqrArr.append(i*i)
        
        sqrArr.sort()
        return sqrArr