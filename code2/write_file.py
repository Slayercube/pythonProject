# write a file

# text = 'Hello, this is a test file\nhow are you doing?\nhave anice day'
#
# with open('test.txt', 'w') as file:
#     file.write(text)
#     print('file written successfully')

# amending the file

text = '\nI am adding this line to the file second tie\nI hope you are doing well\nhave a nice day\n'
with open('test.txt', 'a') as file:
    file.write(text)
    print('file written successfully')