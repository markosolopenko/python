from pprint import pprint

def fibonacci(n):
    dictionary = {}
    assert n >= 0
    if n < 2:
        dictionary[n] = n
        return dictionary
    else:
        dictionary[n] = fibonacci(n-1) + fibonacci(n-2)
        return dictionary


pprint(fibonacci(12))