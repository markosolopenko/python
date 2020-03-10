import random
import math
def is_valid_word(word,hand):
    with open('words.txt', 'r') as file:
        content = file.read()
    content = content.lower()
    if word not in content.split():
        return False
    for a in word:
        if a not in hand:
            return False
    return True
print(is_valid_word('ted','ediaitt'))