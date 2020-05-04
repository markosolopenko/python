def simplify(number):
    if number <= 0:
        return ''
    s = str(number)
    string = ''
    a = 1
    indx = 0
    length = len(s)
    for char in s:
        if indx != length - 1:
            if char == '0':
                a += 1
                indx += 1
            else:
                string += char + '*' + '1' + '0' * (length - a) + '+'
                a += 1
                indx += 1
        else:
            if char != '0':
                string += char
    if string[-1] is '+':
        return string[:-1]
    return string

