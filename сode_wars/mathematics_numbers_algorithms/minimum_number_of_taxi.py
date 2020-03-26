def min_num_taxis(requests):
    resume = len(requests)
    if len(requests) == 1:
        return 1
    else:
        for a in range(len(requests)):
            for index in range(len(requests)):
                if index == len(requests):
                    break
                if requests[a][1] + 1 == requests[index][0]:
                    resume -= 1
                    continue
        return resume





if __name__ == '__main__':
    print(min_num_taxis([(1,4), (2, 9), (3, 6), (5, 8)]))
