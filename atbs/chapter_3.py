
def collaz(number):
    if number % 2 == 0:
        number = number // 2
        # print(number)
        return number
    else:
        number = 3 * number + 1
        # print(number)
        return number


def call_collaz_until_one(number):
    s = collaz(number)
    while s != 1:
        s = collaz(s)
        print(s)


if __name__ == "__main__":
    number = int(input())
    call_collaz_until_one(number)
