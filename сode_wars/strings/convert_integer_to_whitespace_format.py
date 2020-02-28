def whitespace_number(n):
    space_tab_lf_string = ''
    s = bin(n)
    arr = []
    if n == 0:
        return "[space][tab]"
    for char in range(len(str(s))):
        arr.append(s[char])
    if '-' in arr:
        space_tab_lf_string += '\t'
        arr.remove("0")
    print(arr)
    for character in range(len(arr)):
        if arr[character] == '0':
            space_tab_lf_string += ' '
        if arr[character] == '1':
            space_tab_lf_string += '\t'
        if character == len(arr) - 1:
            space_tab_lf_string += '\n'

    return space_tab_lf_string\
        .replace(" ", '[space]')\
        .replace("\t", "[tab]")\
        .replace('\n', '[LF]')






# # very good solution!!!
# def whitespace_number(n):
#     if n < 0:
#         return "\t" + bin(n)[3:].replace("0", " ").replace("1", "\t") + "\n"
#     elif n == 0:
#         return " \n"
#     return " " + bin(n)[2:].replace("0", " ").replace("1", "\t") + "\n"


if __name__ == "__main__":
    print(whitespace_number(-1))