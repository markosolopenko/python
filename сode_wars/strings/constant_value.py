def solve(s: str):
    for vowel in 'aeiou':
        s = s.replace(vowel, 'a')
    splits = s.split('a')
    return max([sum([ord(letter) - 96 for letter in letters]) for letters in splits])


if __name__ == "__main__":
    print(solve("zodiacs"))