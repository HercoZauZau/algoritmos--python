num=cont=soma=0
while num!=999:
    soma+=num
    cont+=1
    num=int(input('Digite um número [999 = Parar] » '))
cont-=1
print('Você digitou {} números e o somatório é {}'.format(cont,soma))
