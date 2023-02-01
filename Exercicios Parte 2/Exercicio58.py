from random import randint
x=randint(0,10)
conty=1
y=int(input('''Jogo Iniciado!
Adivinhe o número que eu escolhi entre 0 e 10: '''))
while y is not x:
    if y<x:
        y=int(input('Mais... Tente novamente: '))
    else:
        y=int(input('Menos... Tente novamente: '))
    conty+=1
print('Acertou! Com {} tentativas.'.format(conty))
