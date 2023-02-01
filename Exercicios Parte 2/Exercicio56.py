somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
mulher20=0
for p in range(1,5):
    print('{} PESSOA:'.format(p))
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip()
    somaidade+=idade
    if p==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        mulher20+=1
mediaidade=somaidade/4
print('''A média de idade do grupo é de {} anos.
O Homem mais velho tem {} anos e se chama {}.
Ao todo são {} mulheres com menos de 20 anos.'''.format(mediaidade,maioridadehomem,nomevelho,mulher20))
