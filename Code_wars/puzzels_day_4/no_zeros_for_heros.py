def no_boring_zeros(n):
    if n == 0:
        return 0
    return int(str(n).rstrip("0"))


if  __name__ == "__main__":
    print(no_boring_zeros(100021450000))