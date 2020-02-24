import numpy


def main():
    print("Put x: ")
    x = int(input())
    print("Put y: ")
    y = int(input())
    print(x**y)
    print(numpy.log(x))


if __name__ == "__main__":
    main()


wins = 0
losses = 0
ties = 0
print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
