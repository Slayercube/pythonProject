# tuple = collection which is ordered and unchangeble
#          used to group toghter related data

student = ('deep',31,'male')
print(student.count('deep'))
print(student.index('male'))
for i in student:
    print(i)

if 'deep' in student:
    print('deep is here')