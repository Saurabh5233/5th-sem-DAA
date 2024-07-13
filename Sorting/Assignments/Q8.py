# https://leetcode.com/problems/height-checker/description/

# Height checker

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Create the expected list by sorting the heights list
        expected = sorted(heights)
        count = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count