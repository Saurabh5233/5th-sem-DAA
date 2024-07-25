# https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1


# Minimum Cost of ropes



import heapq

class Solution:
    def minCost(self, arr, n):
        # Create a min-heap from the given array of rope lengths
        heapq.heapify(arr)
        
        total_cost = 0
        
        # Continue until the heap has more than one rope
        while len(arr) > 1:
            # Extract the two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Combine the ropes
            cost = first + second
            total_cost += cost
            
            # Insert the combined rope back into the heap
            heapq.heappush(arr, cost)
        
        return total_cost

# Example usage:
sol = Solution()
print(sol.minCost([4, 3, 2, 6], 4))  # Output: 29
print(sol.minCost([4, 2, 7, 6, 9], 5))  # Output: 62
