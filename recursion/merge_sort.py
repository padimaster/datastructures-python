# Sumar todos los numeros naturales anteriores usando recursividad
# Input: 10
# Output: 55
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
import traceback


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    while i < len(left):
        result.append(left[i])
        i = i + 1

    while j < len(right):
        result.append(right[j])
        j = j + 1

    return result


def merge_sort(unsorted):

    if len(unsorted) == 1:
        return unsorted

    middle = len(unsorted) // 2
    left = merge_sort(unsorted[:middle])
    right = merge_sort(unsorted[middle:])

    together = merge(left, right)
    return together


def solve(numbers):
    # Retorno
    return merge_sort(numbers)


# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [[5, 3, 4, 6, 2, 1, 8, 9, 7]]

    expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

    for i in range(len(test_cases)):
        solution = None
        try:
            test_case = test_cases[i]

            solution = solve(test_case)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(
                f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")
        except Exception as error:
            print(traceback.format_exc())


main()
