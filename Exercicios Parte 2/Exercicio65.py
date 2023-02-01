x='S'
maior=menor=soma=cont=0
while x=='S':
 num=int(input('Digite um número: '))
 cont+=1
 soma+=num
 x=input('Continuar? [S/N] » ').strip().upper()[0]
 if cont==1:
     maior= menor =num
 else:
     if num>maior:
         maior=num
     if num<menor:
            menor=num
 while x not in 'SN' or x=='':
     print('Escolha apenas S ou N')
     x=input('Continuar? [S/N] » ').strip().upper()[0]
 if x=='N':
      print('''Você digitou {} números e a média foi {:.1f}
O maior nº é {} e o menor é {}'''.format(cont,(soma/cont),maior,menor))
