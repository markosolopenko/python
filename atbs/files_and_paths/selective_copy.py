import os
import shutil
from pathlib import Path
import glob
from pprint import pprint
def copy():
    #os.mkdir("give_me_files")
    print(Path.cwd())
    for certain_files in os.walk(os.getcwd()):
        certain_files = glob.glob('*.txt')
    for file in certain_files:
        shutil.copy(file,'/home/marko/projects/crash/atbs/intresting_things/give_me/')

if __name__ == "__main__":
    copy()