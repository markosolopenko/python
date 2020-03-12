def solve(s: str):
    vowels = "aeiou"
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    constant_of_value = []
    count = 0
    for letter in s:
        if letter in vowels:
            s = s.replace(letter,'a')
    s = s.split('a')
    for letter in s:
        for close in letter:
            count += alphabet.index(close) + 1
        constant_of_value.append(count)
        count = 0
    return max(constant_of_value)
if __name__ == "__main__":
    print(solve("zodiacs"))