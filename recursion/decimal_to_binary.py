# Convertir un decimal a binario usando recursividad
# Input: 10
# Output: 1010

import traceback


def decimal_to_binary(decimal):
    # Casos base

    # Algoritmo

    return


def solve(decimal):
    # Llamada a la funcion recursiva

    # Retorno
    return 


# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [10, 20, 233, 1525]
    expected = [1010, 10100, 11101001, 10111110101]

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
