def delete_nth(order,max_e):
    without_reordering = []
    for i in order:
        if without_reordering.count(i) >= max_e:
            continue
        else:
            without_reordering.append(i)
    return without_reordering


if __name__ == '__main__':
    print(delete_nth([20, 37, 20, 21], 1))