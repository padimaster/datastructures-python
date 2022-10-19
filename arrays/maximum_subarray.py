# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
# and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def kadane(array):
    max_so_far = max_ending_here = array[0]

    for i in range(1, len(array)):
        max_ending_here += array[i]

        if max_ending_here < array[i]:
            max_ending_here = array[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far


# Driver program to test maxSubArraySum
data = [-2, -3, -2, -1, 2, -1,4]
print(kadane(data))
