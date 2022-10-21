# A string is given. We have to print the reversed string.
# For example, the string is "Hi how are you?"
# The output should be "?ouy era woh iH"
import traceback

def solve(string):
    len_string = len(string)
    # Simular un arreglo estatico
    # string_list = [None for _ in range(len_string)]

    left_pointer = 0
    right_pointer = len_string - 1

    string_list = list(string)
    while(left_pointer < len_string // 2):
        left_value = string_list[left_pointer]
        string_list[left_pointer] = string_list[right_pointer]
        string_list[right_pointer] = left_value

        # O equivalente
        # string_list[left_pointer], string_list[right_pointer] = (
        #     string_list[right_pointer],
        #     string_list[left_pointer],
        # )

        left_pointer += 1
        right_pointer -= 1

    return "".join(string_list)

# def solve(string):
#     len_string = len(string)

#     reserved_string = []
#     for i in range(len_string - 1, -1, -1):
#         current_char = string[i]
#         reserved_string.append(current_char)

#     return "".join(reserved_string)

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
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

main()