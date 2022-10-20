# os для управления файлами и каталогами
import os
from pprint import pprint

pprint(os.listdir(os.getcwd()))

for path, dirs, files in os.walk('.'):
    pprint(path)
    pprint(dirs)
    pprint(files)