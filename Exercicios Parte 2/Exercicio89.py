cont = ' '
ln = []  # Lista de Nomes
lm = []  # Lista de Médias
lv = []  # Lista de Valores (notas)
lista = []  # Lista Composta
cnt = aluno = 0
while cont not in 'Nn':
    cnt += 1
    nome = input('\033[1mNome: ')
    ln.append(nome)
    n1 = float(input('Nota 1: '))
    lv.append(n1)
    n2 = float(input('Nota 2: '))
    lv.append(n2)
    lista.append(lv[:])
    lv.clear()
    lm.append((n1 + n2) / 2)
    cont = input('Continuar? [S/N]')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>4}')
print('-' * 20)
for pos in range(0, cnt):
    print(f'{pos:<4}{ln[pos]:<10}{lm[pos]:>4}')
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('Finalizado.')
        break
    print(f'Notas de {ln[aluno]} são {lista[aluno]}')
    print('-' * 40)
