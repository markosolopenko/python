def send(string: str):
    binary_format = ''
    for letter in string:
        bins = format(ord(letter), 'b')
        if len(bins) < 7:
            binary_format += '0' + bins
        else:
            binary_format += bins
    new_string = ''
    for num in range(len(binary_format)):
        if num == len(binary_format) - 1:
            new_string += binary_format[num]
            break
        if binary_format[num] == '1' and binary_format[num+1] == '0' or binary_format[num] == '0' and binary_format[num + 1] == '1':
            new_string += binary_format[num] + ' '
        else:
            new_string += binary_format[num]
    unary_format = ''
    for char in new_string.split(' '):
        if '1' in char:
            length = '0'*len(char)
            unary_format += '0 ' + length + ' '
        if '0' in char:
            length = '0'*len(char)
            unary_format += '00 ' + length + ' '
def receive(string: str):
    bin_string = ''
    string = string.split()
    a = 0
    while a < len(string):
        if len(string[a]) == 1:
            string[a+1] = '1'*len(string[a+1])
            bin_string += string[a+1]
            a += 2
        elif len(string[a]) == 2:
            string[a+1] = '0'*len(string[a+1])
            bin_string += string[a+1]
            a += 2
    binary_separate = ''
    indx = 0
    length = 0
    while indx < len(bin_string):
        if length == 7:
            binary_separate += ' '
            length = 0
        binary_separate += bin_string[indx]
        indx += 1
        length += 1
    ascii_string = ''
    for binary in binary_separate.split(" "):
        s = chr(int(binary, 2))
        ascii_string += s
    return ascii_string
if __name__ == "__main__":
    print(send("Chuck Norris' keyboard has 2 keys: 0 and white space."))
    print(receive('0 0 00 0000 0 000 00 0000 0 00'))


