def tower_builder(n_floors):
    string = ''
    arr = []
    c = 1
    s = ''
    some = '*'
    ls = list(range(1, n_floors + 1))
    for a in range(len(ls)):
        if a == len(ls)-1:
            string += some
            arr.append(string)
            break
        else:
            mid = ((int(ls[-1]) * 2 - 1) - (int(ls[a]) * 2 - 1)) // 2
            string += ' '*mid + some + ' '*mid
            arr.append(string)
            some += '**'
            string = ''
    return arr