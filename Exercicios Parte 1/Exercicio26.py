x=(input('Digite uma frase:').upper()).strip()
print('A letra (A) aparece {} vezes.'.format(x.count('A')))
print('A letra (A) aparece pela 1ª vez na {}ª posiçao.'.format(x.find('A')+1))
print('A letra (A) aparece pela ultima vez na {}ª posiçao'.format(x.rfind('A')+1))
