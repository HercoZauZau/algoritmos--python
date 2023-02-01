x=str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while x not in 'MF':
    x=str(input('Dado inválido. Tente novamente: ')).strip().upper()[0]
print('Dado {} registado com sucesso.'.format(x))

# Usamos o '[0]' para válidar apenas a 1ª letra da string. Por exemplo, se o usuario digitar 'Masculino', apenas o 'M' será lido e o programa vai reconhecer como dado válido.
