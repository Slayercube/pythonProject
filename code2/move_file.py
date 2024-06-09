import os

source = 'test.txt'
destination = 'C:\\Users\\dkcri\\Desktop\\test.txt'

try:
     if os.path.exists(destination):
        print('File already exists')
     else:
         os.replace(source, destination)
         print(source+'File moved')

except FileNotFoundError:
    print(source+'File not found')
