import random
x=random.randint(0,5)
y=int(input('De 0 a 5, adivinhe qual numero eu escolhi:'))
print('CORRECTO!' if y==x else 'ERRADO!')
