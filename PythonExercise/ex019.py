from random import choice
s1 = str(input('Type the first name: '))
s2 = str(input('Type the second name: '))
s3 = str(input('Type the third name: '))
s4 = str(input('Type the fourth name: '))
list = [s1,s2,s3,s4]
print('The classmate chosen is {}'.format(choice(list)))