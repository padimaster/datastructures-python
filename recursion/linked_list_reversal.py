# Sumar todos los numeros naturales anteriores usando recursividad
# Input: 10
# Output: 55
# Explanation:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
import traceback


def reversal_list():
    return


def solve(list_to_reverse):
    # Retorno
    return 


# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [{
        "value": 1,
        "next": {
            "value": 2,
            "next": {
                "value": 3,
                "next": {
                    "value": 4,
                    "next": None,
                },
            },
        },
    }]

    expected = [[1, 2, 3, 4]]

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
