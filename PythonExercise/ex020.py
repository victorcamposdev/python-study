from random import shuffle 
a1 = str(input('type the first name: '))
a2 = str(input('Type the second name: '))
a3 = str(input('Type the third name: '))
a4 = str(input('Type the fourth name: '))
list = [a1, a2, a3, a4]
shuffle(list)
print('The order wil be: {}'. format(list))
