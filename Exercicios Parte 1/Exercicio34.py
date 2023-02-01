x = float (input ('Digite o salario:'))
if x <= 1250:
    y = x + (x * 15 / 100)
else:
    y = x + (x * 10 / 100)
print ('O seu salario de RS{} passa a ser RS{}'.format (x, y))
