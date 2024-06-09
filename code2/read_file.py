
try:
    with open('C:\\users\\dkcri\\Desktop\\text.txt')as file:
        print(file.read())
        print(file.name)
        print(file.mode)
    print(file.closed)
except FileNotFoundError:
    print('file not found')
except SyntaxError:
    print('syntax error')