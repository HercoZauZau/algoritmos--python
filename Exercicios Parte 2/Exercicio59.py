print('\033[1;30;44m  CALCULADORA  \033[m')
from time import sleep
primero=int(input('Digite o primeiro valor: '))
segundo=int(input('Digite o segundo valor: '))
lista=1
while lista in [1,2,3,4,5]:
    lista=int(input('''   [1] Somar
   [2] Multiplicar
   [3] Maior
   [4] Novos números
   [5] Sair do programa
Qual é a sua opção? » '''))
    if lista==1:
        print('A soma de {} e {} é {}.'.format(primero,segundo,primero+segundo))
        print('='*40)
        sleep(2)
    elif lista==2:
        print('O produto de {} e {} é {}.'.format(primero,segundo,primero*segundo))
        print('='*40)
        sleep(2)
    elif lista==3:
        if primero>segundo:
            print('{} é maior que {}.'.format(primero,segundo))
        elif segundo>primero:
            print('{} é maior que {}.'.format(segundo,primero))
        else:
            print('{} é igual a {}.'.format(primero,segundo))
        print('='*40)
        sleep(2)
    elif lista==4:
        primero=int(input('Digite o primeiro valor: '))
        segundo=int(input('Digite o segundo valor: '))
    elif lista==5:
        lista=0
        print('\033[31mFinalizando...\033[m')
        sleep(2)
        print('\033[31mFim do Programa.\033[m')
    else:
        print('\033[31mEscolha apenas dentre as opções acima!\033[m')
        lista=1
        sleep(2)
