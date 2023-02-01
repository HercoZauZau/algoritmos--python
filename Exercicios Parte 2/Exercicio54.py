from datetime import date
ano=date.today().year
menor=0
maior=0
for x in range(1,8):
    y=int(input('Digite o ano de nascimento da {}ª pessoa: '.format(x)))
    idade=ano-y
    if idade<18:
        menor+=1
    else:
        maior+=1

print('{} pessoas são maiores de idade e {} são menores de idade.'.format(maior,menor))
