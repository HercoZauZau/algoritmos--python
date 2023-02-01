from usuario import moeda

prc = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(prc)} é {moeda.moeda(moeda.metade(prc))}')
print(f'O dobro de {moeda.moeda(prc)} é {moeda.moeda(moeda.dobro(prc))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(prc, 10))}')
