def fibonacci(n):
    a, b = 0, 1
    while True:
        if a > n:
            raise StopIteration()
        yield a
        a, b = b, a + b

print sum([fib for fib in fibonacci(4000000) if fib % 2 == 0])
