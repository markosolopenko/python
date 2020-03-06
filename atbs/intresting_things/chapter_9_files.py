#### Current directory and chage it
from pathlib import Path
from os import path
#print(Path.cwd())
# print(os.chdir(path=))
###### Home directory
#print(Path.home())
##### Make new folder
#os.makedirs('C:\\delicious\\walnut\\waffles')
### Check if path is absolute or not
# Path.cwd().is_absolute()
# print(os.path.abspath('.'))
# sonnetFile = open('/home/marko/projects/crash/mit_programming/WordsForGames.txt')
# print(sonnetFile.readlines())

##### Shelve
# import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

################     ORGANIZING FILES    ###############
import shutil
# p = path.realpath('some.txt.txt')
# b = shutil.move('some.txt.txt', 'some.txt')
# print(b)
#### Delete files with send2trash
import send2trash
# new = open('some.txt','a')
# new.write('Hello world')
# new.close()
# send2trash.send2trash('some.txt')


### Walk through folder(files and folders in this folder)
# import os
# for folderName, subfolders, filenames in os.walk(os.getcwd()):
#     print('The current folder is ' + folderName)
#
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#
#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)
#
#     print('')

####### ZIP Files
import zipfile, os
from pathlib import Path
p = Path.home()
p = p/'projects'/'crash'/'atbs'

example_zip = zipfile.ZipFile('some.zip','w')
example_zip.write('chapter_9_files.py',compress_type=zipfile.ZIP_DEFLATED)
example_zip.close()
example_zip.namelist()
