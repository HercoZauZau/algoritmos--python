def factorial(n, show=False):   # "Show" é uma variável qualquer que criamos para usar em condições. Se "Show=True" então o programa segue o caminho X.
    """
    # Calcula o factorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) Mostra a equação.
    :return: O valor do factorial de um número n.
    """
    c = 1
    for contagem in range(n, 0, -1):
        if show:
            print(contagem, end='')
            if contagem > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        c *= contagem
    return c


# Programa Principal
print(factorial(5, show=True))
help(factorial)
