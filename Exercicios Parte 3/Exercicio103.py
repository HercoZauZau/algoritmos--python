def ficha(x, y):
    if x.isalpha():
        x = nome
    else:
        x = '<desconhecido>'
    if y.isnumeric():
        y = gols
    else:
        y = 0
    return print(f'O jogador {x} fez {y} gol(s) no campeonato.')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

ficha(nome, gols)
