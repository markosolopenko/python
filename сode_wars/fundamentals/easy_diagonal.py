def diagonal(n, p):
    num = n
    croc = 1
    sum_of_diagonals = 0
    amount_of_diagonals = 0
    while amount_of_diagonals <= p:
        for char in range(1,num,croc):
            print(char)
            sum_of_diagonals += char
        amount_of_diagonals += 1
        croc +=1
        num -= 1
    return sum_of_diagonals + n

if __name__ == "__main__":
    print(diagonal(20,5))