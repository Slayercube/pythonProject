# copyfile() method is used to copy the content of one file to another file.
# copy()= copyfile() + permission mode + destination file is overwritten if it already exists.
# copy2()= copy() + file metadata is copied.

import shutil

shutil.copyfile('test.txt', 'copy.txt')  # test.txt is copied to copy.txt

print("File copied successfully")