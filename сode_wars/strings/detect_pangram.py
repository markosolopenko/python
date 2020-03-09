import string
def is_pangram(current_sentence: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in current_sentence.lower():
            return False
    return True

if __name__ == "__main__":
    print(is_pangram(current_sentence="The quick, brown fox jumps over the lazy dog!"))