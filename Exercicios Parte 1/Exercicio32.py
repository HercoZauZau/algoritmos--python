from datetime import date
x=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if x==0:
    x=date.today().year
if x%4==0 and x%100!=0 or x%400==0:
    print('O ano {} e BISSEXTO'.format(x))
else:
    print('O ano {} nao e BISSEXTO'.format(x))
