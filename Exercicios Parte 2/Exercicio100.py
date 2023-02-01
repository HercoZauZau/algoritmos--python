from random import randint
from time import sleep

lista = []


def sorteio(x):
    print(f'Sorteando {x} valores da lista: ', end='')
    for num in range(0, x):
        aleatorio = randint(0, 9)
        lista.append(aleatorio)
        sleep(0.25)
        print(aleatorio, end=' ', flush=True)    # O "Flush" serve para que o laço For não acumule o tempo do Sleep.
    print('PRONTO!')


def soma_par(x):
    cont = 0
    for num in lista:
        if num % 2 == 0:
            cont += num
    print(f'Somando os valoes pares de {lista}, temos {cont}.')


sorteio(8)
soma_par(lista)
