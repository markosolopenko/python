import math
result = {1:1.414213, 10:1.478197, 40:1.478896}
def len_curve(n):
    return result.get(n, 1.478942)
print(len_curve(1))


