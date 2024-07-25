# https://www.geeksforgeeks.org/problems/shortest-job-first/1

# Shortest Job first



def solve(bt):
    bt.sort()  # Sort burst times
    ct = [0] * len(bt)  # Completion times
    wt = [0] * len(bt)  # Waiting times
    
    # Calculate completion times
    ct[0] = bt[0]
    for i in range(1, len(bt)):
        ct[i] = ct[i - 1] + bt[i]
    
    # Calculate waiting times
    for i in range(len(bt)):
        wt[i] = ct[i] - bt[i]
    
    # Calculate average waiting time
    total_wt = sum(wt)
    avg_wt = total_wt / len(bt)
    
    return avg_wt

# Example burst times
bt = [4, 2, 3, 1]
print("Average Waiting Time:", solve(bt))
