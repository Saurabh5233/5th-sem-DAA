# https://leetcode.com/problems/maximum-units-on-a-truck/description/

# Maximum Units on a Truck
from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the boxes based on units per box in descending order
        boxTypes.sort(reverse=True, key=lambda x: x[1])
        
        maxUnits = 0
        
        for box in boxTypes:
            boxCount, unitsPerBox = box
            
            if truckSize >= boxCount:
                # If the truck can carry all boxes of this type
                maxUnits += boxCount * unitsPerBox
                truckSize -= boxCount
            else:
                # If the truck can only carry part of the boxes of this type
                maxUnits += truckSize * unitsPerBox
                truckSize = 0
                break
        
        return maxUnits

        
        