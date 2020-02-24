"""
Extra Perfect Numbers (Special Numbers Series #7)
Finding all odd numbers in this number range and adding to list
"""
def extra_perfect(n):
    c = []
    for a in range(n + 1):
        if a % 2 != 0:
            c.append(a)
    return c
print(extra_perfect(28))

