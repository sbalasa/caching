from .caching import lru_cahce, memoize
from timeit import timeit


@lru_cache(None)
def fib_lru_cache(n):
"""
Generate fibonacci series using lru caching mechanism
"""
if n == 0:
    return [0]
elif n == 1:
    return [1]
else:
    fib_series = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        fib_series.append(a)
    return fib_series

@memoize
def fib_memoized_cache(n):
"""
Generate fibonacci series using memoized caching
"""
if n == 0:
    return [0]
elif n == 1:
    return [1]
else:
    fib_series = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        fib_series.append(a)
    return fib_series
 

def test_lru_caching():
    print(timeit("fib_lru_cache(100)", setup = "from __main__ import fib_lru_cache"))

def test_memoized_caching():
    print(timeit("fib_memoized_cache(100)", setup = "from __main__ import fib_memoized_cache"))


if __name__ == "__main__":
    test_lru_caching()
    test_memoized_caching()
