# https://www.geeksforgeeks.org/problems/shop-in-candy-store1145/1

# Shop in Candy Store


class Solution:

    def candyStore(self, candies,N,k):
        candies.sort()
        #   N= len(candies)
          # compute Min price
        min_p = 0
        buy =0
        free = N-1
        
        while(buy<= free):
            min_p += candies[buy]
            buy+=1
            free-=k
          # compute Max price
        max_p = 0
        buy = N-1
        free = 0
        while free<= buy:
            max_p += candies[buy]
            buy -=1
            free+=k
          
        return min_p, max_p