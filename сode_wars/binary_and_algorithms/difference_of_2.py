def twos_difference(lst):
    return sorted((i, i+2) for i in lst if i + 2 in lst)



if __name__ == '__main__':
    print(twos_difference([1,2,3,4]))