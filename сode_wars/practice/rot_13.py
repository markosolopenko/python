def rot13(message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = "!@#$%^&*()_-+={}[]."
    rot = ''
    for char in message:
        if char == ' ':
            rot += char
        elif char.isdigit():
            rot += char
        elif char in symbols:
            rot += char
        else:
            orda = ord(char.lower()) % 97
            res = (orda + 13) % len(alphabet)
            if char.isupper():
                rot += alphabet[res].upper()
            else:
                rot += alphabet[res].lower()
    return rot


if __name__ == '__main__':
    print(rot13('Test'))