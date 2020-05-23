import re


def calculate_string(st):
    operator = re.findall(r'\+|-|/|\*', st)
    st = st.split(''.join(operator))
    left_part_numbers = re.findall(r'[0-9.]', st[0])
    right_part_numbers = re.findall(r'[0-9.]', st[-1])
    if ''.join(operator) == '+':
        return str(round(float(''.join(left_part_numbers)) + float(''.join(right_part_numbers))))

    elif ''.join(operator) == '/':
        return str(round(float(''.join(left_part_numbers)) / float(''.join(right_part_numbers))))

    elif ''.join(operator) == '-':
        return str(round(float(''.join(left_part_numbers)) - float(''.join(right_part_numbers))))

    elif ''.join(operator) == '*':
        return str(round(float(''.join(left_part_numbers)) * float(''.join(right_part_numbers))))



if __name__ == '__main__':
    print(calculate_string(";$%§fsdfsd235??df/sdfgf5gh.000kk0000"))