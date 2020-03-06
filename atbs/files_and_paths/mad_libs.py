from pathlib import Path
from pprint import pprint


def mad_libs():

    with open('text004.txt', 'r') as file:

    with open('data/text.txt', 'r') as file:

        context = file.read()
        for line in context.split():
            if "ADJECTIVE" in line:
                prompt = input("Enter the adjective:\n")
                context = context.replace("ADJECTIVE", prompt, 1)
            elif "NOUN" in line:
                prompt = input("Enter the noun:\n")
                context = context.replace("NOUN", prompt, 1)
            elif "VERB" in line:
                prompt = input("Enter the verb:\n")
                context = context.replace("VERB", prompt, 1)
        pprint(context)

    with open('text004.txt', 'a') as some:


    with open('data/text.txt', 'a') as some:

        some.write(context)
        # some.close() automatically closed


if __name__ == "__main__":
    mad_libs()