from pathlib import Path
from pprint import pprint
import re
import os
import glob


def regex_search():
    for filename in glob.glob('*.txt'):
        with open(filename, 'r') as file:
            content = file.read()
            matches = re.findall(r'\d{3}-\d{3}-\d{4}', content)
            if matches:
                pprint(matches)


if __name__ == "__main__":
    regex_search()