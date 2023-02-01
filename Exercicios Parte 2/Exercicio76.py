print('\033[1m')
lista=('Pão',10,'Tomate',20,'Leite',100,'Arroz',1000,'Rachel',100,'Ovos',65,'Sumo',100,'Manteiga',85,'Chá',65,'Café',60)
print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('='*40)
for pos in range(0,len(lista)):
    if pos%2==0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('='*40)
