import math
a = float(input('Digite o comprimento do cateto oposto:'))
b = float(input('Digite o comprimento do cateto adjacente:'))
c = math.sqrt((a**2)+(b**2))
print('O comprimento da hipotenusa e {:.1f}'.format(c))
