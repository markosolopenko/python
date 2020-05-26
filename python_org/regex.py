import re


def change_all_occur(word_to_find):
    with open('file.txt', 'r') as file:
        res = file.read()
    change_words = re.sub(word_to_find, len(word_to_find)*'*', res)

    with open('file.txt', 'w') as file:
        change = file.write(change_words)
    return change


if __name__ == '__main__':
    print(change_all_occur('Ipsum'))