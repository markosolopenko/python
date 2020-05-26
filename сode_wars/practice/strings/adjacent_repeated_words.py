def count_adjacent_pairs(st):
    count = 0
    check = []
    if st:
        st = st.lower().split()
        for i in range(len(st)):
            if st[i] not in check:
                check = []
                check.append(st[i])
            elif st[i] in check and check.count(st[i]) < 2:
                count += 1
                check.append(st[i])
        return count
    return count


if __name__ == '__main__':
    print(count_adjacent_pairs("dog dog cat cat wolf wolf"))