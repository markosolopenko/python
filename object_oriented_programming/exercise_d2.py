from pprint import pprint
import functools
import timeit


def memoized(func):

    cache_results = {}

    @functools.wraps(func)
    def cache(*args):
        if cache_results:
            return cache_results[args]
        result = func(args)
        cache_results[args] = result
        return result
    return cache()


@memoized
def fibonacci(n):
    if n > 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

s = memoized(fibonacci)
print([s(a) for a in range(12)])