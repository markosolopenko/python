from itertools import groupby


def elves_look_then_say(sequence):
    for i in range(50):
        sequence = ''.join(str(len(list(g)))+k for k, g in groupby(sequence))

    return len(sequence)


if __name__ == '__main__':
    print(elves_look_then_say('1113122113'))

