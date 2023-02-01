lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continua = input('Quer continuar? [S/N] ').upper()
    while continua not in 'SN':
        continua = input('Quer continuar? \033[1;31m[S/N]\033[m ').upper()
    if continua == 'N':
        break
print(f'Você digitou {cont} elemento(s).')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
print('O valor 5 faz parte da lista.'if 5 in lista else 'O valor 5 não faz parte da lista.')
