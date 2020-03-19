from decorators.trying_create_some_decorators import count_calls
import time
import functools

def cache(func):
    """
    Creat my own decorator for keep a cache of previous function calls
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)




@functools.lru_cache(maxsize=4)
def fibonacci(num):
    """
    The cache info with 'lru_cache' decorator instead writing my own
    """
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(12))
print(fibonacci(13))



if __name__ == '__main__':
    start = time.time()
    print(fibonacci(12))
    end = time.time()
    s = end - start
    print(f'{s} sec')

    start = time.time()
    print(fibonacci(12))
    end = time.time()
    s = end - start
    print(f'{s} sec')
    print(fibonacci(14))
    print(fibonacci(11))