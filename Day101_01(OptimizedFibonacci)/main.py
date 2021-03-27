def fibonacci(n):
    global fib_dict
    if n in fib_dict:
        return fib_dict[n]
    else:
        if n == 0:
            fib_dict[n] = 0
            return 0
        elif n == 1 or n == 2:
            fib_dict[n] = 1
            return 1
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
            fib_dict[n] = result
            return result


fib_dict = {}
print(f"Fibonacci(0):{fibonacci(0)}")
print(fib_dict)
print(f"Fibonacci(1):{fibonacci(1)},")
print(fib_dict)
print(f"Fibonacci(6):{fibonacci(420)}")
print(fib_dict)