soma=0
cont=0
for c in range(1,501,2):
    if c%3==0:
        cont=cont+1
        soma=soma+c
print('A soma é {} e os números repeten-se {} vezes.'.format(soma,cont))
