"""
If firs word (istitle) return list all (title) and without nay characters only letters
"""

def to_camel_case(text):
    for letters in text:
        if letters.isalpha():
            continue
        s = text.replace(letters, ",")
        text = s
    split_text = text.split(",")
    if split_text[0].istitle() == False:
        return split_text[0] + ''.join(char.title() for char in split_text[1:])
    else:
        return ''.join(character.title() for character in split_text)

if __name__ == "__main__":
    print(to_camel_case('the_stealth_warrior'))