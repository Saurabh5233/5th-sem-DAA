# we do not compare teh elements directly , but their properties

nums = [473,91,21,45,6,32]

from typing import List

def counting_sort_for_radix(nums: List[int], exp: int) -> List[int]:
    n = len(nums)
    output = [0] * n  # Output array to hold the sorted array
    count = [0] * 10  # Count array to store count of occurrences of digits (0 to 9)

    # Store count of occurrences in count[]
    for i in range(n):
        index = nums[i] // exp
        count[index % 10] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = nums[i] // exp
        output[count[index % 10] - 1] = nums[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to nums[], so that nums[] contains sorted numbers
    for i in range(n):
        nums[i] = output[i]

def radix_sort(nums: List[int]) -> List[int]:
    # Find the maximum number to know the number of digits
    max_num = max(nums)

    # Do counting sort for every digit. Note that instead of passing the digit number, exp is passed.
    # exp is 10^i where i is the current digit number
    exp = 1
    while max_num // exp > 0: 
        counting_sort_for_radix(nums, exp)
        exp *= 10

    return nums

# Example usage
nums = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_nums = radix_sort(nums)
print(sorted_nums)


