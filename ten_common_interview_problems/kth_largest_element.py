# Dado un arreglo de numeros y un entero k, devolver el elemento kth mas grande
# del arreglo

# Ejemplo:
# Input:
#    a = [5,3,6,9,8,7]
#    target = 5
# Output: 5

# Explanation:
# 1st largest element is 9
# 2nd largest element is 8
# 3rd largest element is 7
# 4th largest element is 6
# 5th largest element is 5
import traceback


def solve(numbers, k):
    numbers.sort(reverse=True)
    
    return numbers[k - 1]

# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [{"numbers": [5, 3, 6, 9, 8, 7], "k": 5}]
    expected = [5]

    for i in range(len(test_cases)):
        solution = None
        try:
            test_case = test_cases[i]
            numbers = test_case["numbers"]
            k = test_case["k"]
            solution = solve(numbers, k)

            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(
                f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}"
            )
        except Exception as error:
            print(traceback.format_exc())


main()
