from usuario import moeda

prc = float(input('Digite o preço: '))
print(f'A metade de {prc} é {moeda.metade(prc)}')
print(f'O dobro de {prc} é {moeda.dobro(prc)}')
print(f'Aumentando 10%, temos {moeda.aumentar(prc, 10)}')
