#Dado un arreglo de enteros, encontrar si se encuentran elementos duplicados
#Se debe retornar verdadero si almenos un elemento se repite una vez y falso 
#si todos los elementos son distintos
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false
import traceback

def solve(numbers):
    memo = {}
    
    for number in numbers:
        if number in memo:
            return memo[number]
        
        memo[number] = True

    return False

# Execute the solution function with test cases and verify that the response is the same as expected
def main():
  test_cases = [[1,1,2,3,4,5,6,7,8,9], [1,2,3,4]]
  expected = [True, False]

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


