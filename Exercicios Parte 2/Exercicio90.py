x={}

x['Nome'] = input('Nome: ')
x['Media'] = float(input(f'Média de {x["Nome"]}: '))
if x['Média'] < 7:
    x['Situação'] = 'Reporovado'
else:
    x['Situação'] = 'Aprovado'
for k, v in x.items():
    print(f'{k} é igual a {v}')
