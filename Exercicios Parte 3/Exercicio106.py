from time import sleep


def manual(cmd):
    print('\033[1;30;46m-' * 40)
    print(f"Acessando o manual do comando '{cmd}'")
    print('-' * 40)
    print('\033[m')
    sleep(1)
    print('\033[1;40;37m')
    help(cmd)
    print('\033[m')


while True:
    print('\033[42;30;1m-' * 40)
    print(f'{"SISTEMA DE AJUDA PyHELP":^40}')
    print('-' * 40)
    print('\033[m')
    x = input('Função ou Biblioteca > ')
    if x == 'fim':
        print('\033[1;30;41m-' * 40)
        print(f'{"Até logo.":^40}')
        print('-' * 40)
        print('\033[m')
        break
    else:
        manual(x)
