def binomialCoeff(n, k):
    sums = 0
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k+1):
        res = res * (n - i)
        res = res // (i + 1)
        sums += res

    return sums




if __name__ == "__main__":
    #print(diagonal(2,5))
    print(binomialCoeff(20,4))