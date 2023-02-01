def notas(*num, sit=False):
    """
    # Função para analisar notas e situação de alunos.
    :param num: Uma ou mais notas do aluno (aceita variáveis).
    :param sit: Mostrar a situação (valor opcional).
    :return: Dicionário com informações do estado das notas do aluno.
     04.08.2020
    """
    book = {'Total': len(num),
            'Maior': max(num),
            'Menor': min(num),
            'Média': float(f'{(sum(num)/len(num)):.2f}')}
    if sit:
        if book['Média'] < 5:
            situacao = 'RUIM'
        elif 8 > book['Média'] >= 5:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'BOA'
        book['Situação'] = situacao
    return book


# Programa Principal
resp = notas(7, 8, 9, 10, sit=True)
print(resp)
help(notas)
