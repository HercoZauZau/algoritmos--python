print('\033[1m-' * 40)
print(f'{"MEGA SENA":^40}')
print('-' * 40)

from random import randint
from time import sleep

lista = []
sub = []
n = int(input('Quantos jogos você quer que eu sorteie? '))
for jogo in range(0, n):
    for rand in range(0, 6):
        sub.append(randint(1, 61))
    sub.sort()
    lista.append(sub[:])
    sub.clear()
    print(f'Jogo {jogo+1}: {lista[jogo]}')
    sleep(1)
print('\033[m')
