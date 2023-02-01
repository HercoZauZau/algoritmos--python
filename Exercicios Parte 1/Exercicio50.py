soma=0
cont=0
for c in range(1,7):
    x=int(input('Digite o {}º número:'.format(c)))
    if x%2==0:
        soma+=x
        cont+=1
print('Voce digitou {} números Pares e a soma foi {}'.format(cont,soma))
