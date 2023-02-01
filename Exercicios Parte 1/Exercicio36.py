print('\033[34;44m \033[m'*32)
print(' '*10,'\033[1;30mECOIN BANK\033[m',' '*10)
print('\033[34;44m \033[m'*32)
print('\033[30mEmpréstimo para compra de imóvel...\033[m')
a=str(input('\033[30mPor favor, digite seu nome completo:\033[m')).split()
b=float(input('\033[30mPor favor, digite o valor do imóvel:\033[m'))
c=int(input('\033[30mEm quantas prestaçoes anuais pretende pagar?\033[m'))
d=float(input('\033[30mPor favor, digite o seu salário:\033[m'))
# Introduçao (parte externa)

x=(b/(c*12))
if (b/(c*12))<=(0.3*d):
    print('\033[32mCaro cliente {}. O seu empréstimo foi aprovado. A sua prestaçao mensal será de {:.2f}\033[m'.format(a[len(a)-1],x))
else:
    print('\033[31mCaro cliente {}. Infelizmente o seu salário nao pode cobrir o emprestimo.\033[m'.format(a[len(a)-1]))
print('Atenciosamente... ECOIN BANK.')
