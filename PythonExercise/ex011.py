w = float(input('Type the width of the wall: '))
h = float(input('Type the height of the wall: '))
area = w * h
print('Your wall have {} by {} dimension, and a area of {}m². \nFor you paint the wall, wil need {:.3f}l of paint.'.format(w, h, area,(area / 2)))