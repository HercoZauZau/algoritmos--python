def leiaint(x):
    num = input(x)
    while num.isnumeric() is False:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        num = input(x)
    return int(num)


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
