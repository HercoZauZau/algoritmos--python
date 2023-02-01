print('\033[1m[PEDRA PAPEL TESOURA]\033[m')

import random
y=['Pedra','Papel','Tesoura']
z=(random.choice(y))

x=int(input('''Escolha a sua jogada:
[0] PEDRA
[1] PAPEL
[2] TESOURA
» '''))
if x>2:
    print('Voce só pode escolher uma das opções acima.')
else:
    if x==0:
        print('Voce escolheu Pedra. O computador escolheu {}. Voce '.format(z),end='')
        if z=='Pedra':
            print('empatou.')
        elif z=='Papel':
            print('perdeu.')
        else:
            print('ganhou.')
    elif x==1:
        print('Voce escolheu Papel. O computador escolheu {}. Voce '.format(z),end='')
        if z=='Pedra':
            print('ganhou.')
        elif z=='Papel':
            print('empatou.')
        else:
            print('perdeu.')
    else:
        print('Voce escolheu Tesoura. O computador escolheu {}. Voce '.format(z),end='')
        if z=='Pedra':
            print('perdeu.')
        if z=='Papel':
            print('ganhou.')
        else:
            print('empatou.')
