print('\033[1mCOMPARAR\033[m')
x=int(input('Digite um número inteiro:'))
y=int(input('Digite outro número inteiro:'))
if x>y:
    print('O primeiro valor é maior.')
if y>x:
    print('O segundo valor é maior.')
if x==y:
    print('Nao existe valor maior, os dois sao iguais.')
