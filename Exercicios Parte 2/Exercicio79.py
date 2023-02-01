lista=[]
while True:
    valor=int(input('Digite um valor: '))
    if valor not in lista:
      lista.append(valor)
      print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont=input('Deseja coninuar? [S/N] ').strip().upper()
    if cont=='N':
        print('='*40)
        break
print(f'Você digitou os valores {sorted(lista)}')
