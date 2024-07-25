# https://leetcode.com/problems/insert-interval/description/

# Insert Interval

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_intervals = []
        i, n = 0, len(intervals)
        
        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])
            i += 1
        
        # Merge all overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged new interval
        merged_intervals.append(newInterval)
        
        # Add all intervals that start after the new interval ends
        while i < n:
            merged_intervals.append(intervals[i])
            i += 1
        
        return merged_intervals
