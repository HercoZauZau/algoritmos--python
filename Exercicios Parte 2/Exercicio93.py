play = {}
list = []

play['Nome'] = input('Nome do Jogador: ')
p = int(input(f'Quantas paridas {play["Nome"]} jogou? '))
for g in range(0, p):
    list.append(int(input(f'   Quantos gols na partida {g+1}? ')))
play['Gols'] = list[:]
play['Total'] = sum(list)
print('='*60)
print(play)
print('='*60)
for k, v in play.items():
    print(f'{k} » {v}')
print('='*60)
print(f'O jogaddor {play["Nome"]} jogou {p} partidas.')
for k, v in enumerate(play['Gols']):
    print(f'    »Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {sum(list)} gols.')
