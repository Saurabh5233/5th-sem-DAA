# https://leetcode.com/problems/non-overlapping-intervals/description/


# Non-overlapping Intervals

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize the end time of the last added interval
        end = intervals[0][1]
        count = 0
        
        # Traverse through the sorted intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # Overlapping interval found, increment the count
                count += 1
            else:
                # No overlap, update the end time
                end = intervals[i][1]
        
        return count
