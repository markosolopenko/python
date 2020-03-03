def sum_fracts(lst):
    array_chiselnuk = []
    array_znamennuk = []
    for a in lst:
        for b in a:
            array_chiselnuk.append(a[0])
            array_znamennuk.append(a[1])
if __name__ == "__main__":
    print(sum_fracts([[1, 3], [5, 3]]))