# https://www.geeksforgeeks.org/problems/check-if-it-is-possible-to-survive-on-island4922/1

# Check if it is possible to survive on Island
import math
class Solution:
    def minimumDays(self, S, N, M):
        sundays = S//7
        buy_days = S - sundays
        total_food = S*M
        total_days = math.ceil(total_food/N)
        if total_days <= buy_days:
          return total_days
        else:
          return -1
