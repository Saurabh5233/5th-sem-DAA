# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

# Fractional Knapsack

def fractional_knapsack(values:list[int],weight:list[int], c:int)->double:
  N  = len(values)
  items =[[weights[i], values[i]] for i in range(N)]
  # Sort the items on value per unit of weight
  items.sort(reverse=True, key = lambda x:x[1]/x[0])
  total_value = 0.0
  current_w = 0
  for item in items:
    w,v  = item[0], item[1]
    if current_w +w <=c:
      total_value += v
      current_w += w
    else:
      total_value += v*((c - current_w)/w)
      break
  return total_value
