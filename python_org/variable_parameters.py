import math
def variable_func(*args):
    raise_to_pow = 1
    sum_of_elements = 0
    for number in args:
        sum_of_elements += number**raise_to_pow
        raise_to_pow += 1
    return pow(math.sqrt(sum_of_elements), raise_to_pow)


if __name__ == '__main__':
    print(variable_func(3, 4))