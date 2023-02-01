print('\033[1mCadastre uma pessoa')
maior18=0
homem=0
mu20=0

while True:
    print('-'*30)
    i=int(input('Idade: '))
    if i>=18:
        maior18+=1
    s=input('Sexo [M/F]: ').strip().upper()[0]
    if s=='M':
        homem+=1
    if i<20 and s=='F':
        mu20+=1
    print('-'*30)
    x=input('Quer continuar? [S/N]: ').strip().upper()[0]
    if x=='N':
        break
print(f'Total de maiores de 18 anos: {maior18} pessoas.')
print(f'Total de Homens: {homem}')
print(f'Total de Mulheres menores de 20 anos: {mu20} mulheres.')
