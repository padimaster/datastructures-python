# Invertir el string ingresado utilizando recursividad
# Input: Hello
# Output: olleH

import traceback

def recursive():
    # Casos base

    # Algoritmo 

    return 

def solve(string):
    # Llamada a la funcion recursiva

    # Retorno
    return 


# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = ["Hi how are you?", "Hello"]
    expected = ["?uoy era woh iH", "olleH"]

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
