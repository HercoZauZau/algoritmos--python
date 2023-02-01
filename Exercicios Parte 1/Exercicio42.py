x=float(input('Primeiro segmento:'))
y=float(input('Segundo segmento:'))
z=float(input('Terceiro segmento:'))
if x<y+z and y<x+z and z<x+y:
    print('Os segmentos acima podem formar um triangulo ',end='')
    if x==y==z:
        print('Equilátero.')
    elif x!=y!=z!=x:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Os segmentos acima não podem formar um triangulo.')
