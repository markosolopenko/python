import re


with open('puzzle.txt', 'r') as file:
    puzzles = file.read().splitlines()


addresses_separated = [re.split(r'\[|\]', line.strip()) for line in puzzles]

supernet = [' '.join(line[::2]) for line in addresses_separated]
hypernet = [' '.join(line[1::2]) for line in addresses_separated]


def abba(net):
    return any(a + b == d + c and a != b
               for a, b, c, d in zip(net, net[1:], net[2:], net[3:]))


def puzzle1():
    print(sum(abba(sup) and not abba(hyp)
              for sup, hyp in zip(supernet, hypernet)))


def ssl(sup, hyp):
    return any(a == c and a != b and b+a+b in hyp
               for a, b, c in zip(sup, sup[1:], sup[2:]))


def puzzle2():
    print(sum(ssl(sup, hyp) for sup, hyp in zip(supernet, hypernet)))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
