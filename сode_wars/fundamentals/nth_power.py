"""
N-th Power
We should to find index(n) in list and to lift it to degree n
"""
def index(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n]**n
print(index([1, 2, 3, 4],2))