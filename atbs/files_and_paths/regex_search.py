from pathlib import Path
from pprint import pprint
import re
import os
import glob
def regex_search():
    for filename in glob.glob('*.txt'):
        with open(filename,'r') as file:
            content = file.read()
            file.close()
            mathes = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', content)
            pprint(mathes)

if __name__ == "__main__":
    regex_search()