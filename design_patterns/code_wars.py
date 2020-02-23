"""First"""
def extra_perfect(n):
    c = []
    for a in range(n + 1):
        if a % 2 != 0:
            c.append(a)
    return c
print(extra_perfect(28))
"""Second"""
def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000
print(past(0,1,1))
"""Third"""
def max_multiple(divisor, bound):
    a = 0
    while a < len(range(divisor, bound + 1)):
        if bound % divisor == 0:
            return bound
        bound -= 1
        a += 1
print(max_multiple(3,10))
"""Fourth"""

"""the Fifth"""
def index(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n]**n
print(index([1, 2, 3, 4],2))