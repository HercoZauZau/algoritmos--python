tup=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezasseis','Dezassete','Dezoito','Dezanove','Vinte')
x=int(input('Digite um número entre 0 e 20 » '))
while x>20 or x<0:
    x=int(input('Tente Novamente. Digite um número entre 0 e 20 » '))
print(tup[x])
