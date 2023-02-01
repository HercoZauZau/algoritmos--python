from usuario import moeda

prc = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(prc)} é {moeda.metade(prc, True)}')
print(f'O dobro de {moeda.moeda(prc)} é {moeda.dobro(prc, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(prc, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(prc, 13, True)}')
