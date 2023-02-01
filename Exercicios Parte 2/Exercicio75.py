tup= (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))
print(f'O valor 9 apareceu {tup.count(9)} vez(es).')
print(f'O valor 3 aparece na {tup.index(3)+1}ª posição.' if 3 in tup else 'O valor 3 não aparece em nenhuma posição.')
print('Os valores pares digitados foram ',end=' ')
for x in tup:
    if x%2==0:
        print(x,end=' ')
