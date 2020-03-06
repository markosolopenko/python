import os
import shutil
from pathlib import Path
import glob
from pprint import pprint
def delete():
    total_size = 0
    string = ''
    for path, dirs, files in os.walk('/home/marko/projects/crash/atbs/'):
        for file in files:
            filename = os.path.join(path, file)
            total_size += os.path.getsize(filename)
            string += f'Size of <{file}> is: ({total_size} megabite)\n'
        print(string)
        string = ''
    print(f'The total size of {Path.cwd()} folder is {total_size}')


if __name__ == "__main__":
    delete()