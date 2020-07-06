import string


def covered_pawns(pawns):
    cover = 0
    alphabet = string.ascii_lowercase

    for index_i, el_i in enumerate(pawns):
        for j in range(len(pawns)):
            if alphabet[alphabet.index(el_i[0]) - 1] == pawns[j][0] \
                and int(el_i[-1]) + 1 == int(pawns[j][-1]) and index_i != j:
                    # or alphabet[alphabet.index(el_i[0]) - 1] == pawns[j][0]:
                    # and int(el_i[-1]) - 1 == int(pawns[j][-1]):
                cover += 1
            elif alphabet[alphabet.index(el_i[0]) + 1] == pawns[j][0] \
                and int(el_i[-1]) + 1 == int(pawns[j][-1]) and index_i != j:
                    # or alphabet[alphabet.index(el_i[0]) + 1] == pawns[j][0] \
                    # and int(el_i[-1]) - 1 == int(pawns[j][-1]):
                cover += 1
    return cover


if __name__ == '__main__':
    print(covered_pawns(['e5', 'b2', 'b4', 'g4', 'a1', 'a5']))