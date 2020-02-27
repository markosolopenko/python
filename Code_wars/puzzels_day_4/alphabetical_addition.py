import string
def add_letters(*letters):
    alphabet = string.ascii_lowercase
    if not letters:
        return "z"
    a = 0
    for letter in letters:
        a += (alphabet.index(letter)+1)
    return alphabet[(a - 1)%26]

if __name__ == "__main__":
    print(add_letters('c'))

s = (3 - 1)%26
print(s)