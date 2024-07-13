
# https://leetcode.com/problems/buy-two-chocolates/description/

# Buy Two Chocolates

from typing import List

class Solution:
    def buyChocolates(self, prices: List[int], money: int) -> int:
        # Step 1: Sort the prices array
        prices.sort()
        
        # Initialize the minimum leftover money to the initial amount of money
        min_leftover = money
        
        n = len(prices)
        found = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                total_cost = prices[i] + prices[j]
                if total_cost <= money:
                    min_leftover = min(min_leftover, money - total_cost)
                    found = True
                else:
                    break  
        
        # 
        return min_leftover if found else money
