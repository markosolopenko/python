"""
Find the sum of triangular numbers
[01]
02 [03]
04 05 [06]
07 08 09 [10]
11 12 13 14 [15]
16 17 18 19 20 [21]
"""
def sum_triangular_numbers(n):
    sum = 1
    lista = ''
    num = 0
    for i in range(1, n + 1):
        for j in range(1, i+1):
            lista += str(sum) + " "
            sum += 1
        word = lista.split()
        num += int(word[-1])
        lista = ''
    return num


print(sum_triangular_numbers(34))

# easier solution
def sum_triangular_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * (i + 1) // 2
    return sum

