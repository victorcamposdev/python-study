a = float(input('Type the days ranted: '))
b = float(input('Type the Km driven: '))
c = (a * 60) + (b * 0.15)
print('The total is ${:.2f}'.format(c))