par = []
impar = []
for pos in range(1, 8):
    num = int(input(f'Digite o {pos}º valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'Os valores pares digitados foram {sorted(par)}')
print(f'Os valores ímpares digitados foram {sorted(impar)}')
