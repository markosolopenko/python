def how_much(m, n):
    real = []
    moneys = []
    if m > n:
        for money in range(m,n+1,-1):
            for a in range(1,n+1):
                if money - a*7 == 2 or money - a*9 == 1:
                    if money in real:
                        moneys.append(money)
                    real.append(money)
    else:
        for money in range(m,n+1):
            for a in range(1,n+1):
                if money - a*7 == 2 or money - a*9 == 1:
                    if money in real:
                        moneys.append(money)

                    real.append(money)
    real = []
    array = []
    for mon in moneys:
        array.append("M: " + str(mon))
        for j in range(1,n):
            if int(mon) - j * 7 == 2:
                array.append("B: " + str(j))
            if int(mon) - j * 9 == 1:
                array.append("C: " + str(j))
        array[1], array[-1] = array[-1],array[1]
        real.append(array)

        array = []
    return real

if __name__ == "__main__":
    print(how_much(10000, 9950))