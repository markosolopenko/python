from pathlib import Path
from pprint import pprint
def mad_libs():
    with open('text.txt', 'r') as file:
        context = file.read()
        for line in context.split():
            if "ADJECTIVE" in line:
                prompt = input("Enter the adjective:\n")
                context = context.replace("ADJECTIVE", prompt)
            elif "NOUN" in line:
                prompt = input("Enter the noun:\n")
                context = context.replace("NOUN", prompt)
            elif "VERB" in line:
                prompt = input("Enter the verb:\n")
                context = context.replace("VERB", prompt)
        pprint(context)
    with open('text.txt','a') as some:
        some.write(context)
        some.close()

if __name__ == "__main__":
    mad_libs()