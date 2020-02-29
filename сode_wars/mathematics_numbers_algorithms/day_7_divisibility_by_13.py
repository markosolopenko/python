def thirt(n):
    n = str(n)[::-1]
    sum_of_divide = 0
    pattern = [1, 10, 9, 12, 3, 4]
    index_pattern = 0
    sum_of_end = 0
    while True:
        for index_n in range(len(n)):
            if index_pattern == len(pattern):
                index_pattern = 0
                sum_of_divide += int(n[index_n]) * pattern[index_pattern]
                index_pattern += 1
            else:
                sum_of_divide += int(n[index_n]) * pattern[index_pattern]
                index_pattern += 1
        index_pattern = 0
        if int(sum_of_end) == int(sum_of_divide):
            return sum_of_end
        sum_of_end = sum_of_divide
        n = str(sum_of_divide)[::-1]
        sum_of_divide = 0

if __name__ == "__main__":
    print(thirt(85299258))