def longest_repetition(chars):
    if chars == '':
        return ('', 0)
    arr = []
    curr = ''
    count = 1
    for i in chars:
        if i == curr:
            count += 1
        else:
            arr.append((curr, count))
            count = 1
            curr = i
    arr.append((curr, count))
    arr = sorted(arr, key=lambda x: x[1])
    for j in range(1, len(arr)):
        if arr[j][1] == arr[-1][1]:
            return arr[j]
    return arr[-1]


if __name__ == '__main__':
    print(longest_repetition("ba"))