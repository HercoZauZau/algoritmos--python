matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Colocamos os zeros dentro das listas para não usarmos o "append()", nesse caso, os valores recebidos vão substituir os zeros.
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para [{linhas};{colunas}]: '))
# Cada linha gerada vai gerar 3 colunas em ordem, preenchendo cada posição em MATRIZ. Perceba a ordem dos laços para facilitar.
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
    print()
    # O último espaço em branco serve para quebrar o END=
