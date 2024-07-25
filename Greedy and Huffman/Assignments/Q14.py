# https://leetcode.com/problems/merge-intervals/description/
# Merge Intervals

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If the list is empty, return it
        if not intervals:
            return []
        
        # Sort the intervals based on the start times
        intervals.sort(key=lambda x: x[0])
        
        # Initialize the result list with the first interval
        merged_intervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # Get the last interval in the result list
            last_interval = merged_intervals[-1]
            current_interval = intervals[i]
            
            # Check if the current interval overlaps with the last interval in the result
            if current_interval[0] <= last_interval[1]:
                # Merge the intervals by updating the end time of the last interval
                last_interval[1] = max(last_interval[1], current_interval[1])
            else:
                # No overlap, add the current interval to the result list
                merged_intervals.append(current_interval)
        
