print('\033[1;30m[CÁLCULO DO IMC]\033[m')
x =float(input('Qual é seu peso?'))
y =float(input('Qual é sua altura?'))
imc=x/(y**2)
print('O seu IMC é de {:.2f}. O seu estado é de '.format(imc),end='')
if imc<18.5:
    print('\033[4mabaixo do peso\033[m.')
elif imc>=18.5 and imc<25:
    print('\033[4mpeso ideial\033[m.')
elif imc>=25 and imc<30:
    print('\033[4msobrepeso\033[m.')
elif imc>=30 and imc<=40:
    print('\033[4mobesidade\033[m.')
else:
    print('\033[4mobesidade mórbida.\033[m')
