def cache_decorator(f):
    cache = {}

    def g(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return g


@cache_decorator
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


for i in range(0, 1000):
    print(fib(i))
