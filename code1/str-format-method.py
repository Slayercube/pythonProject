# str.format = this method allows users to have more control over
#              displaying infiomation


# item1 = 'cow'
# item2 = 'moon'

# text = 'my {moon} jump over the {moon}'
# print(text.format(cow='cow', moon='moon'))

# padding
# text = 'my {} jump over the {:10}. how cow'
#
# print(text.format(item1,item2))

number = 3.4363
number1 = 1000
# print('this number is: {}'.format(number))
# print('this number is: {:.2f}'.format(number))
# print('this number is: {:,}'.format(number1))
print('this number is: {:b}'.format(number1))