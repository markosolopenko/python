def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    print(s)
    return palindrom(s[1:-1])


if __name__ == '__main__':
    print(palindrom('lhsdffdshl'))
    # s = 'sdffds'
    # print(s[1:-1])