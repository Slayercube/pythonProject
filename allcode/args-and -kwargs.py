# *args = parameter that will pack all argument into a tuple
#         useful so that function can ac pet varying amount of argument

# def add(*args):
#     sum = 0
# # sinch you cant change tuple have to convert it into list to change it
#     args = list(args)
#     args[0] = 3
#     for i in args:
#          sum += i
#     return sum
# print(add(1,2,3,4,5))

# **kwargs = parameter that will pack all argument into a dictionary

def hello(**kwargs):
    # print('hello '+ kwargs['first' ]+ kwargs['middle']+ kwargs['last'])
    for key, value in kwargs.items():
        print(value, end=' ')


hello(title='Mr.', first='deep', middle='sidhu', last='yoyo')
