print('\033[1m««CONTROLE DE IDADE»»\033[m')
x=int(input('Digite seu ano de nascimento » '))
import datetime
y=datetime.date.today().year
z=y-x
if z<=9:
    print('Atleta \033[4mMirim\033[m.')
if z>9 and z<=14:
    print('Atleta \033[4mInfantil\033[m.')
if z>14 and z<=19:
    print('Atleta \033[4mJúnior\033[m.')
if z==20:
    print('Atleta \033[4mSénior\033[m.')
if z>20:
    print('Atleta \033[4mMaster\033[m.')
print('Obrigado.')
