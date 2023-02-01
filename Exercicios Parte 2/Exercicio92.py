from datetime import date

job = {'Nome': input('Nome: '),
       'Idade': date.today().year - (int(input('Ano de nascimento: '))),
       'CTPS': int(input('Carteira de Trabalho (0 » não tem): '))}


if job['CTPS'] != 0:
    job['Ano de Contracto'] = int(input('Ano de contratação: '))
    job['Salário'] = int(input('Salário: R$'))
    job['Anos até aposentadoria'] = 70 - job['Idade']
else:
    job['CTPS'] = 'Não tem.'


print('=' * 40)

for k, v in job.items():
    print(f'{k}: {v}')

