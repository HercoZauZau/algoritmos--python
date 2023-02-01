a= int(input('Primeiro valor:'))
b= int(input('Segundo valor:'))
c= int(input('Terceiro valor:'))
# Verificando o menor
x=a
if b<a and b<c:
    x=b
if c<a and c<b:
    x=c
# Verificando o maior
y=a
if b>a and b>c:
    y=b
if c>a and c>b:
    y=c
print('O maior valor e {}'.format(y))
print('O menor valor e {}'.format(x))
