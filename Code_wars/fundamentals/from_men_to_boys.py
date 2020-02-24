"""Sort Out from Men to Boys"""
def men_from_boys(arr):
    odd = set()
    even = set()
    for a in arr:
        if a % 2 == 0:
            even.add(a)
        else:
            odd.add(a)

    return sorted(even) + sorted(odd, reverse=True)
print(men_from_boys([20,33,50,34,43,46]))