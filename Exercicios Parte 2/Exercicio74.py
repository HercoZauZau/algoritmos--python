from random import randint

cont = maior = menor = 0
while cont < 5:
    rand = randint ( 0,9 )
    print ( rand,end=' ' )
    cont += 1
    if cont == 1 or rand < menor:
        menor = rand
    if cont == 1 or rand > maior:
        maior = rand
print ( f'\nMaior valor: {maior}' )
print ( f'Menor valor: {menor}' )
