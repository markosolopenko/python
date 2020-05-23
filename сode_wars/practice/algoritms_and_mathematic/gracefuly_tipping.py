import math


def graceful_tipping(bill):
    if bill <= 10:
        return math.ceil(bill + (bill*15/100))
    else:
        res = math.ceil(bill + (bill*15/100))
        num = int('5' + ('0' * (len(str(res)) - 2) ))
        while res % num != 0:
            res += 1
        return res


if __name__ == '__main__':
    print(graceful_tipping(7))