def max_profit(prices):
    array = []
    array_less = []
    for a in range(len(prices)-1):
        if max(prices[a+1:]) > prices[a]:
            array.append(max(prices[a+1:]) - prices[a])
        else:
            array_less.append(max(prices[a+1:]) - prices[a])
    if array:
        return max(array)
    return max(array_less)


if __name__ == '__main__':
    print(max_profit([10, 7, 5, 8, 11, 9]))