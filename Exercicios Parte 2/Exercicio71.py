print('\033[44m \033[m'*30)
print(' '*9, '\033[1mECOIN BANK\033[m')
print('\033[44m \033[m'*30)

valor = int(input('Digite o valor a sacar: R$'))

c50 = valor//50
if c50 != 0:
    print(c50, 'Cédula(s) de R$50')
c20 = valor % 50
if c20//20 != 0:
    print(c20//20, 'Cédula(s) de R$20')
c10 = c20 % 20
if c10//10 != 0:
    print(c10//10, 'Cédula(s) de R$10')
c1 = c10 % 10
if c1//1 != 0:
    print(c1//1, 'Cédula(s) de R$1')
