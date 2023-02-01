from random import randint
from operator import itemgetter

jogo={'J1': randint(1, 6),
      'J2': randint(1, 6),
      'J3': randint(1, 6),
      'J4': randint(1, 6)}
ranking=[]
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

# sorted(jogo.items(), key=itemgetter(1), reverse=True) - Organiza os itens em ordem decrescente.
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
