def wave_sort(a):
    a.sort(reverse=True)
    copy = a[:]
    switch = True
    indx = 0
    while switch:
        if len(copy) < 2:
            if copy:
                for c in copy:
                    a[indx] = c
                    indx+=1
            switch = False
        else:
            a[indx] = copy.pop(0)
            indx += 1
            a[indx] = copy.pop(-1)
            indx+=1


if __name__ == '__main__':
    print(wave_sort([1, 1, 1, 1]))
