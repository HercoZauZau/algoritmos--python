def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m2.')


print(f'\033[1m{"Controle de Terrenos":^30}')
print('_'*30)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)
