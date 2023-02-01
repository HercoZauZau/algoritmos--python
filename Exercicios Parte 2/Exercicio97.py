print('\033[1m')
# Para deixar o programa em negrito.


def escreva(txt):
    linhas = len(txt) + 8
    print('-' * linhas)
    print(f'{txt:^{linhas}}')
    print('-' * linhas)


# Programa principal.
escreva('Olá, mundo!')
escreva('Curso em Vídeo.')
