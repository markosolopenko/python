def next_higher(value):
    value_in_bin = bin(value)
    amount_of_one = value_in_bin.count('1')
    some = True
    value = value + 1
    while some:
        new_value_bin = bin(value)
        if new_value_bin.count('1') == amount_of_one:
            some = False
        else:
            value += 1
    return value

if __name__ == '__main__':
    print(next_higher(1))
