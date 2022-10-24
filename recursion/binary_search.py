# Sumar todos los numeros naturales anteriores usando recursividad
# Input: 10
# Output: 55
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
import traceback


def binary_search(numbers, left, right, target):
    # Casos base
    if left > right:
        return 1

    mid = (left + right) // 2

    if target == numbers[mid]:
        return mid

    if target < numbers[mid]:
        return binary_search(numbers, left, mid - 1, target)

    if target > numbers[mid]:
        return binary_search(numbers, mid + 1, right, target)


def solve(numbers, target):
    # Retorno
    return binary_search(numbers, 0, len(numbers) - 1, target)


# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [{
        "numbers": [-23, -10, -3, -1, 0, 4, 10, 203],
        "target": -3
    }]

    expected = [2]

    for i in range(len(test_cases)):
        solution = None
        try:
            test_case = test_cases[i]
            numbers = test_case["numbers"]
            target = test_case["target"]

            solution = solve(numbers, target)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(
                f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")
        except Exception as error:
            print(traceback.format_exc())


main()
