lista=[]
maxpos=[]
minpos=[]
for x in range(0,5):
    lista.append(int(input('Digite um número: ')))
print(lista)
print(f'O maior valor da lista é {max(lista)} \nO menor valor da lista é {min(lista)}')
for indice,valor in enumerate(lista):
    if valor==max(lista):
        maxpos.append(indice+1)
    if valor==min(lista):
        minpos.append(indice+1)
print(f'{max(lista)} está nas posições {maxpos}.\n{min(lista)} está nas posições {minpos}.')
