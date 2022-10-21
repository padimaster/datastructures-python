import traceback

def solve(case):
    return 1

# Execute the solution function with test cases and verify that the response is the same as expected
def main():
  test_cases = [3, 5, 7, 9, 13]
  expected = [3, 8, 21, 55, 377]

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