import math
def diagonal(row, index):
    row= row+1
    index = index+1
    tb = math.factorial(row)/math.factorial(row-index)
    tb = int(tb) / math.factorial(index)
    return int(tb)




if __name__ == "__main__":
    print(diagonal(20,15))
