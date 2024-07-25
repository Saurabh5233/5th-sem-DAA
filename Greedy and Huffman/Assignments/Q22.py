# https://www.geeksforgeeks.org/problems/assign-mice-holes3053/0

# Assign mice holes



def assignMiceHoles(N, M, H):
    # Sort both arrays
    M.sort()
    H.sort()
    
    # Calculate the maximum distance
    max_distance = 0
    for i in range(N):
        max_distance = max(max_distance, abs(M[i] - H[i]))
    
    return max_distance

# Example usage:
print(assignMiceHoles(3, [4, -4, 2], [4, 0, 5]))  # Output: 4
print(assignMiceHoles(2, [4, 2], [1, 7]))         # Output: 3
