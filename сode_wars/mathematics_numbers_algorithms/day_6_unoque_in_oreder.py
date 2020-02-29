def unique_in_order(iterable):
    unique_character = []
    for unique in range(len(iterable)):
        if unique == len(iterable) - 1:
            unique_character.append(iterable[unique])
            break
        if iterable[unique] == iterable[unique+1]:
            continue
        unique_character.append(iterable[unique])
    return unique_character


if __name__ == "__main__":
    print(unique_in_order('AAAABBBCCDAABBB'))