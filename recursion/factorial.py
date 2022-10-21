import traceback

#Iter Factorial
# def solve(number):
#     result = 1
#     current_number = 1

#     while current_number <= number:
#         result = result * current_number
#         current_number += 1
    
#     return result

def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)

# Execute the solution function with test cases and verify that the response is the same as expected
def main():
  test_cases = [4, 10, 100]
  expected = [24, 3628800, 3628800]

  for i in range(len(test_cases)):
        solution = None
        try:
            test_case = test_cases[i]
    
            solution = factorial(test_case)
          
            assert solution == expected[i]
            print("OK")
        except AssertionError as assert_error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}")            
        except Exception as error:
            print(traceback.format_exc())

main()

    
