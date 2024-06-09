import os

path = 'C:\\Users\\dkcri\\Desktop\\text.txt'

if os.path.exists(path):
    print('file found')
    if os.path.isfile(path):
        print('file is a file')
    elif os.path.isdir(path):
        print('file is a directory')
else:
    print('file not found')