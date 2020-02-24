"""Finding Maximum Multiple for divisor in range(divisor,bound + 1)"""
def max_multiple(divisor, bound):
    """
    :param divisor:
    :param bound:
    :return:
    """
    assert divisor >= bound
    a = 0
    while a < len(range(divisor, bound + 1)):
        if bound % divisor == 0:
            return bound
        bound -= 1
        a += 1
    return None
print(max_multiple(3,10))