def solution(s):
    new = ''
    for char in s:
        if char.isupper():
            new += " "
        new += char
    return new

if __name__ == "__main__":
    print(solution("helloWorldHereWeAre"))