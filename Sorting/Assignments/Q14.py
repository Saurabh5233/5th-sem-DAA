# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/

# Sort Array by Increasing Frequency


from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each element
        freq = Counter(nums)
        
        # Step 2: Sort the elements based on the custom sorting rules
        # We sort by frequency (ascending), then by value (descending)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums
