def group_anagrams(list_of_strings):
    matrix = []
    arr = []
    sorted_elements = sorted([sorted(i) for i in list_of_strings])
    for i in range(len(list_of_strings)):
        if sorted(list_of_strings[i]) == sorted_elements[i]:
            arr.append(list_of_strings[i])
        else:
            matrix.append(arr)
            arr = []
    return matrix

    #
    # for i in range(len(list_of_strings)):
    #     if sorted(list_of_strings[i]) in check:
    #         continue
    #     else:
    #         check.append(sorted(list_of_strings[i]))
    #         arr.append(list_of_strings[i])
    #         for j in range(i+1, len(list_of_strings)):
    #             if sorted(arr[0]) == sorted(list_of_strings[j]):
    #                 arr.append(list_of_strings[j])
    #         matrix.append(arr)
    #         arr = []
    # return matrix


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
