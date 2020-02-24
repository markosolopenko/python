def collaz(number):
    if number % 2 == 0:
        number = number // 2
        return number
    else:
        number = 3 * number + 1
        return number
number = int(input())
s = collaz(number)
while s != 1:
    s = collaz(s)
    print(s)


