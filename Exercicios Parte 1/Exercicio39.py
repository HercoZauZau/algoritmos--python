print('\033[1;42;30m[CONTROLO MILITAR]\033[m')
x=int(input('Digite seu ano de nascimento:'))
import datetime
y=datetime.date.today().year
z=y-x
if z==18:
    print('É a hora de se alistar ao exército. Cumpra com o seu dever, recruta.')
if z>18:
    print('Já passou da hora de se alistar, desertor. Voce devia ter se alistado {} ano(s) atrás.'.format(z-18))
if z<18:
    print('Voce ainda é um bebé. Volte para o colo da mamá e volte daqui a {} anos(s).'.format(18-z))
