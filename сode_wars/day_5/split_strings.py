def solution(s):
    pairs = []
    string = ''
    if len(s) % 2 != 0:
        s += '_'
    for character in s:
        string += character
        if len(string) == 2:
            pairs.append(string)
            string = ''
    return pairs
print(solution("asdfads"))