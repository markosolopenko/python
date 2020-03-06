import os
import re
import shutil
from pathlib import Path
import glob
from pprint import pprint
def rename_files():
    files = re.compile(r"^(.*?)(\d\d\d).(txt$)",re.VERBOSE)
    for name_file in os.listdir('.'):
        mo = files.search(name_file)
        if mo == None:
            continue
        before_part = mo.group(1)
        second_part = mo.group(2)
        third_part = mo.group(3)


        new_name_of_files = before_part + second_part + third_part
        work_dir = os.path.abspath('.')
        name_file = os.path.join(work_dir,name_file)
        new_name_of_files = os.path.join(work_dir,new_name_of_files)

        print(f'Renaming "{name_file}" to "{new_name_of_files}"...')
        shutil.move(name_file, new_name_of_files)
if __name__ == "__main__":
    rename_files()