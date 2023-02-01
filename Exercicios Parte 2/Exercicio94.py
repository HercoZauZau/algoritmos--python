dic={}
pro=' '
list=[]
soma=0

while pro not in 'Nn':
    dic['Nome']=input('Nome: ')
    dic['Sexo']=input('Sexo: [M/F] ').upper()
    while dic['Sexo'] not in 'MF':
        print('\033[1;31mERRO!\033[m Por favor, digite apenas M ou F.')
        dic['Sexo']=input('Sexo: [M/F] ').upper()
    dic['Idade']=int(input('Idade: '))
    soma+=dic['Idade']
    list.append(dic.copy())
    pro=input('Continuar? [S/N] ')
    while pro not in 'SsNn':
        print('\033[1;31mERRO!\033[m Responda apenas S ou N.')
        pro=input('Continuar? [S/N] ')

print(f'A) Ao todo temos {len(list)} pessoas cadastradas.')
print(f'B) A média de idades é de {soma/len(list):.2f} anos.')
print(f'C) As mulheres cadastradas foram ',end='')
for m in list:
    if m['Sexo'] == 'F':
        print(m['Nome'],end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for m in list:
    if m['Idade']>=soma/len(list):
        print('    ',end='')
        for k,v in m.items():
            print(f'{k} » {v}; ', end='')
        print()
