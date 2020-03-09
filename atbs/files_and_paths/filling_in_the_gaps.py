import os
import re
import shutil
from pathlib import Path
import glob
from pprint import pprint
numbers = []
def rename_files():
    files = re.compile(r"^(.*?)(\d\d)(\d).(txt$)",re.VERBOSE)
    for name_file in os.listdir('.'):
        mo = files.search(name_file)
        if mo == None:
            continue
        digit = mo.group(3)
        numbers.append(digit)
    for num in range(len(numbers) - 1):
        if int(numbers[int(num) + 1]) - int(numbers[int(num)]) == 1:
            continue
        else:
            numbers[int(num) + 1] = str(int(numbers[int(num)]) + 1)
    indx = 0
    for name_file in os.listdir('.'):
        certain_files = files.search(name_file)
        if certain_files == None:
            continue
        before_part = certain_files.group(1)
        zeros_part = certain_files.group(2)
        file_type = certain_files.group(4)
        sorted_name_of_files = f'{before_part}{zeros_part}{numbers[indx]}.{file_type}'
        current_directory = os.path.abspath('.')
        name_file = os.path.join(current_directory,name_file)
        sorted_name_of_files = os.path.join(current_directory,sorted_name_of_files)
        shutil.move(name_file,sorted_name_of_files)
        print(f'Renaming "{name_file}" to "{sorted_name_of_files}"...')
        indx += 1







if __name__ == "__main__":
    rename_files()