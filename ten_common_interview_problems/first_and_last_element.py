# Dado un arreglo ordenado y un target, determinar en que posicion del arreglo
# empieza y termina. Si el target no se encuentra en el arreglo, devolver [-1, -1]
#
# Ejemplo
# Input:
#    a = [1,5,5,7]
#    target = 5
# Output: [5, 8]
import traceback


def solve(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1

    left_flag = False
    rigth_flag = False

    while (left_pointer <= right_pointer):
        if not left_flag:
            left_pointer += 1
        
        if numbers[left_pointer] == target:
            left_flag = True
        
        if not rigth_flag:
            right_pointer -= 1
        
        if numbers[right_pointer] == target:
            rigth_flag = True

        if left_flag and rigth_flag:
            break
    
    if left_flag and rigth_flag:
        return [left_pointer, right_pointer]

    return [-1, -1]

# Execute the solution function with test cases and verify that the response is the same as expected
def main():
    test_cases = [{
        "numbers": [1,5,5,7],
        "target": 5
    },{
        "numbers": [1,1,2,3,4,5,5,5,5,7],
        "target": 5
    }]
    expected = [[1,2], [5,8]]

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
                f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}"
            )
        except Exception as error:
            print(traceback.format_exc())


main()
