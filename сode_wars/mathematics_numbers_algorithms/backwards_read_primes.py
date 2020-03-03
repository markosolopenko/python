def backwards_prime(start, stop):
    prime = []
    some = []
    result = []
    fes = []
    for num in range(start,stop):
        if num <= 12 or num % 2 == 0 or str(num) == str(num)[::-1]:
            continue
        for i in range(2,num+1):
            if num % i == 0:
                prime.append(num)
        if len(prime) == 1:
            some.append(prime[0])
            prime = []
        prime = []
    for prim in some:
        prim = str(prim)[::-1]
        for j in range(2, int(prim) + 1):
            if int(prim) % int(j) == 0:
                fes.append(prim[::-1])
        if len(fes) == 1:
            result.append(int(fes[0]))
            fes = []
        fes = []
    return result






if __name__ == "__main__":
    print(backwards_prime(400, 1000))