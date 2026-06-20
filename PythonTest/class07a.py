name = str(input('What is your name: '))
print('Nice to meet you {:20}!'.format(name))
print('Nice to meet you {:>20}!'.format(name))
print('Nice to meet you {:<20}!'.format(name))
print('Nice to meet you {:^20}!'.format(name))
print('Nice to meet you {:=^20}!'.format(name))
n1 = int(input('A value: '))
n2 = int(input('Another value: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('The sum is {}, \nthe product is {} and the quotient is {:.3f}'.format(s, m, d), end='. ')
print('The integer division is {} and power is {}'.format(di, e))