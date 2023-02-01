# Esta resolução não contém lista dentro de lista. A resolução de Guanabara contém.
pesomenor = []
pesomaior = []
c = 0
maior = menor = 0
while True:
    y = input('Nome: ')
    x = float(input('Peso: '))
    c += 1
    if c == 1:
        maior = x
        menor = x
    else:
        if x == maior:
            maior = x
            pesomaior.append(y)
        if x > maior:
            maior = x
            pesomaior.clear()
            pesomaior.append(y)
        if x == menor:
            menor = x
            pesomenor.append(y)
        if x < menor:
            menor = x
            pesomenor.clear()
            pesomenor.append(y)
    cont = input('Continuar? [S/N]')
    if cont in 'Nn':
        break
if c == 1:
    print(f'Foi cadastrada 1 pessoa.\nO peso é {x}Kg.')
else:
    print(f'Foram cadastradas {c} pessoas.')
    print(f'O maior peso é {maior}Kg de {pesomaior}')
    print(f'O menor peso é {menor}Kg de {pesomenor}')
