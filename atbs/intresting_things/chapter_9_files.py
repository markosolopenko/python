#### Current directory and chage it
from pathlib import Path
import os
#print(Path.cwd())
# print(os.chdir(path=))
###### Home directory
#print(Path.home())
##### Make new folder
#os.makedirs('C:\\delicious\\walnut\\waffles')
### Check if path is absolute or not
# Path.cwd().is_absolute()
# print(os.path.abspath('.'))
sonnetFile = open('/home/marko/projects/crash/mit_programming/WordsForGames.txt')
print(sonnetFile.readlines())

##### Shelve
# import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

################     ORGANIZING FILES    ###############
