exp=str(input('Digite uma expressão: '))
print('Sua expressão está válida.' if exp.count('(') == exp.count(')') else 'Sua expressão está inválida!')
