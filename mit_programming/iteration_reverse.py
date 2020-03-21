
some_list = [1, 2, 3, 4, 5, 10]
for a in range(len(some_list) - 1, 0, -1):
    xcount = 0
    indx = 0
    head_list = some_list[indx]
    while xcount != a:
        some_list[indx], some_list[indx + 1] = some_list[indx + 1], some_list[indx]
        xcount += 1
        indx += 1
print(some_list)