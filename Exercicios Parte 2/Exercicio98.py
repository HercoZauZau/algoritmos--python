from time import sleep
lista = []


def linha():
    print('=' * 30)

# Programa de introdução:


linha()
print('Contagem de 1 até 10 de 1 em 1')
for cont in range(1, 11):
    print(cont, end=' ')
print('FIM!')
linha()

linha()
print('Contagem de 10 até 0 de 2 em 2')
for cont in range(0, 11):
    lista.append(cont)
for cont in lista[10::-2]:
    print(cont, end=' ')
print('FIM!')
linha()

# Programa principal:


def contador(inicio, fim, passos):
    if inicio < fim and passos > 0:
        while inicio <= fim:
            print(inicio, end=' ', flush=True)   # O "Flush" serve para que o laço For não acumule o tempo do Sleep.
            sleep(0.5)
            inicio += passos
        print('FIM!')
    elif inicio > fim and passos < 0:
        while inicio >= fim:
            print(inicio, end=' ', flush=True)   # O "Flush" serve para que o laço For não acumule o tempo do Sleep.
            sleep(0.5)
            inicio += passos
        print('FIM!')
    else:
        print(i, 'FIM!')


linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passos: '))
contador(i, f, p)
linha()
