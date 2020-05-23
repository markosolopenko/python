def solve(n):
    if str(n)[-1] != '0':
        return -1
    else:
        count = 0
        bank = [10, 20, 50, 100, 200, 500]
        if n in bank:
            return 1
        res = 0
        t = n
        for i in bank[::-1]:
            if t == 0 or t-i == 0:
                break
            elif t - i > 0:
                count += 1
                res += i
                t -= i
                for _ in range(5):
                    if n-res > i:
                        count += 1
                        res += i
                        t -= i
                    elif n - res == i:
                        count+= 1
                        return count
                    else:
                        break
        return count + 1

if __name__ == '__main__':
    print(solve(1500))