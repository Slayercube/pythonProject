import os
import shutil

# os.remove() method in Python is used to remove or delete a file path.
# os.rmdir() method in Python is used to remove or delete a directory.
# shutil.rmtree() method in Python is used to remove or delete a directory.


path = 'copy.txt'

try:
    if os.path.exists(path):
        os.remove(path)
        print('File deleted')
    else:
        print('File not found')
except FileNotFoundError:
    print('File not found')
