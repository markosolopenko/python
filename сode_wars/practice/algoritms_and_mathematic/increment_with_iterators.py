def increment(number, iterations, spacer):
    position = spacer
    for _ in range(iterations):
        length = len(str(number))
        position = position % length
        number += int(str(1)+'0'*(length - 1 - position))
        position += spacer
        if len(str(number)) > length:
            position += 1
    return number


if __name__ == '__main__':
    print(increment(9999, 9, 9))
