from math import radians, cos, sin, tan
a = float(input('Type a angle: '))
print('The angle of {} have the sine {:.2f}'.format(a, sin(radians(a))))
print('The angle of {} have the cosine {:.2f}'.format(a, cos(radians(a))))
print('The angle of {} have the tangent {:.2f}'.format(a, tan(radians(a))))
