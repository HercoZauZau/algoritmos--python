print('\033[1;30;44m  [SHOPING 21]  \033[m')
barato=z=acima=cont=0
x='S'
pb=''

while x=='S':
 print('\033[1m')
 prdt=input('Nome do Produto: ').strip()
 prc=float(input('Preço: R$'))
 cont+=prc
 z+=1
 if z==1:
     barato=prc
     pb=prdt
 else:
     if prc<barato:
         barato=prc
         pb=prdt
 if prc>1000:
     acima+=1
 x=input('Quer Continuar? [S/N]: ').strip().upper()[0]
 while x not in 'SN':
     x=input('\033[1;31mEscolha apenas uma das opcções » [S/N]: \033[m').strip().upper()[0]
     if x in 'SN':
         break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total da compra: R${cont:.2f}')
print(f'Produtos acima de R$1000: {acima}')
print(f'Produto mais barato: {pb}; Preço: {barato:.2f}')
