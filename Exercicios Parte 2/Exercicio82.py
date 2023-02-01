lista=[]
par=[]
impar=[]
while True:
    num=int(input('Digite um número: '))
    lista.append(num)
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)
    cont=input('Quer continuar? [S/N] ').upper()
    while cont not in 'SN':
        cont=input('Quer continuar? \033[1;31m[S/N]\033[m ').upper()
    if cont=='N':
        break
print(f'Lista completa {lista}\nLista par {par}\nLista ímpar {impar}')
