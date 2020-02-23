"""
Extra Perfect Numbers (Special Numbers Series #7)
"""


def extra_perfect(n):
    """
    :param n:
    :returns:
    """
    list_of_numbers = []
    for a in range(n + 1):
        if a % 2 != 0:
            list_of_numbers.append(a)
    return list_of_numbers


# print(extra_perfect(28))


def past(hours, minutes=0, seconds=0):
    """
    Converts set of hours, minutes and seconds to milliseconds
    :param hours:
    :param minutes:
    :param seconds:
    :return:
    """
    return (hours * 3600 + minutes * 60 + seconds) * 1000


# print(past(3))

# Maximum Multiple
def max_multiple(divisor, bound):
    """

    :param divisor:
    :param bound:
    :return:
    """
    assert bound >= divisor

    a = 0
    while a < len(range(divisor, bound + 1)):
        if bound % divisor == 0:
            return bound
        bound -= 1
        a += 1
    # need extra return statement

# print(max_multiple(3, 2))


"""Sort Out The Men From Boys"""
def men_from_boys(arr):
    odd = set()
    even = set()
    for a in arr:
        if a % 2 == 0:
            # if a in even:
            #     continue
            even.add(a)
        else:
            # if a in odd:
            #     continue
            odd.add(a)

    return sorted(even) + sorted(odd, reverse=True)

print(men_from_boys([20,33,50,34,43,46]))

"""N-th Power"""
def index(array, n):
    if n >= len(array):
        return -1
    else:
        return array[n]**n

# print(index([1, 2, 3, 4],2))