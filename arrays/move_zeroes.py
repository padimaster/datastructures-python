# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
import traceback

def solve(numbers):
    order_pointer = 0

    for idx in range(len(numbers)):
        if numbers[idx] != 0:
            numbers[idx], numbers[order_pointer] = numbers[order_pointer], numbers[idx]
            order_pointer += 1

    return numbers

# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [[0, 1, 0, 3, 12]]
    expected = [[1, 3, 12, 0, 0]]

    for i in range(len(test_cases)):
        solution = None
        try:
            test_case = test_cases[i]

            solution = solve(test_case)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(
                f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}"
            )
        except Exception as error:
            print(traceback.format_exc())


main()

# Hacks
# def one_liner_move(array):
#     array.sort(key=bool, reverse=True)
#     return array
