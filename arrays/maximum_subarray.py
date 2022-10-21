# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
# and return its sum.
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

import traceback


def solve(numbers):
    len_numbers = len(numbers)

    max = -99999999
    for i in range(len_numbers):
        current_amount = 0
        for j in range(i, len_numbers):
            current_amount += numbers[j]
            if current_amount > max:
                max = current_amount

    return max

def kadane(array):
    max_so_far = max_ending_here = array[0]

    for i in range(1, len(array)):
        max_ending_here += array[i]

        if max_ending_here < array[i]:
            max_ending_here = array[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far


# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
    expected = [6]

    for i in range(len(test_cases)):
        solution = None
        try:
            test_case = test_cases[i]

            solution = kadane(test_case)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(
                f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}"
            )
        except Exception as error:
            print(traceback.format_exc())


main()


