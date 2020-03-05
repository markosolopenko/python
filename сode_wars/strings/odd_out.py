from pprint import pprint

def odd_one_out(s: str):
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

if __name__ == "__main__":
    print(odd_one_out('Hello world'))