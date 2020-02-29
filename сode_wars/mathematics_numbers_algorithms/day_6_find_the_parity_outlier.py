def find_outlier(integers):
    odd = []
    even = []
    for num in integers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]

if __name__ == "__main__":
    print(find_outlier([2, 4, 6, 8, 10, 3]))