print('\033[1m[SHOPPING 21]\033[m')
x=float(input('Digite o preço do produto: '))
y=int(input('''Opções de pagamento:
[1] Para pagamento á vista (Dinheiro/Cheque)
[2] Para pagamento á vista (Cartão)
[3] Para pagamento em até 2x no cartão
[4] Para pagmento em 3x ou mais no cartão

Escolha » '''))
if y==1:
    print('Voce recebeu 10% de desconto. O preço final será de {:.1f}'.format(x-(x*0.1)))
elif y==2:
    print('Voce recebeu 5% de desconto. O preço final será de {:.1f}'.format(x-(x*0.05)))
elif y==3:
    print('Sua compra será dividída em duas parcelas de {:.1f} cada. O preço final será de {:.1f}'.format(x/2,x))
elif y==4:
    a=int(input('Em quantas parcelas deseja pagar? '))
    if a<3:
        print('\033[31mNesta opção só pode escolher 3 ou mais parcelas.\033[m')
    else:
        z=((x/a)+(0.2*(x/a)))
        f=z*a
        print('Sua compra será dividída em {} parcelas de {:.1f} cada. O preço final será de {:.1f}'.format(a,z,f))
else:
    print('\033[31mSó pode escolher uma das opções acima.\033[m')


