from time import sleep


def linha():
    print('=-=' * 20)


def maior(*num):
    linha()
    print('Analisando os valores passados...')
    for tupla in num:
        sleep(0.25)
        print(tupla, end=' ', flush=True)   # O "Flush" serve para que o laço For não acumule o tempo do Sleep.
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')


maior(1, 2, 3, 4, 5, 6, 20)
maior(2, 4, 6, 8, 4, 0)
maior(3, 4, 6, 8, 9, 6, 44, 57, 8, 111)
