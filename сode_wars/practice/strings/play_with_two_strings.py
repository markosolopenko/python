def work_on_strings(a, b):
    b = list(b)
    indx = 0
    index = 0
    for i in b:
        if i in a.lower() and a.lower().count(i) % 2 != 0:
            b[indx] = i.upper()
            indx += 1
        elif i.isupper() and i.lower() in a.lower() and a.lower().count(i.lower()) % 2 != 0:
            b[indx] = i.lower()
            indx += 1
        else:
            indx += 1
    b = ''.join(b)
    a = list(a)
    for j in a:
        if j in b.lower() and b.lower().count(j) % 2 != 0:
            a[index] = j.upper()
            index += 1
        elif j.isupper() and j.lower() in b.lower() and b.lower().count(j.lower()) % 2 != 0:
            a[index] = j.lower()
            index += 1
        else:
            index += 1
    return ''.join(a) + b


if __name__ == '__main__':
    print(work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe"))
    #                     "abcDeFGtrzW    DEFGgGFhjkWqE"