print('\033[1;30;47m  [CONVERSOR]  \033[m')
x=int(input('Digite um número inteiro qualquer:'))
print('''Escolha a base de conversao:
[1] para Binário
[2] para Octal
[3] para Hexadecimal''')
y=int(input('» '))
print('\033[1;30m[RESULTADO]\033[m')

if y==1:
    print(bin(x))
elif y==2:
    print(oct(x))
elif y==3:
    print(hex(x))
else:
    print('\033[1;31mEscolha Inválida! Tente Novamente.\033[m')
