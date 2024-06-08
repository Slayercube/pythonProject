import time



rows = int(input('how many rows? :'))
columns = int(input('how many columns? :'))
symbol = input('how many symbols? :')

for i in range(rows):
    for j in range(columns):
        print(symbol , end='')
    print()
