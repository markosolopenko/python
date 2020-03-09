from pprint import pprint

def odd_one_out_s(s: str):
    array = []
    for a in s:
        if s.count(a) % 2 == 0:
            continue
        else:
            array.append(a)
    new_arr = []
    for num in range(len(array)):
        if array.count(array[num]) > 1:
            array[num] = ''
        else:
            new_arr.append(array[num])
    return new_arr
import time
def odd_one_out(s):
    for num in s:
        if s.count(num) % 2 == 0:
            s = s.replace(num, '')
        elif s.count(num) > 1:
            s = s.replace(num, '', s.count(num) - 1)
    return list(s)

if __name__ == "__main__":
    print(odd_one_out('Hello world'))
    print(odd_one_out_s('Hello world'))