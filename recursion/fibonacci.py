def fib(number, memo):
    if number in memo:
        return memo[number]

    if number == 0:
        return 0

    if number == 1:
        return 1

    memo[number] = fib(number - 1, memo) + fib(number - 2, memo)

    return memo[number]

print(fib(9, {}))