tupla=('programador','hacker','filantropia',
       'cleptomania','ceda','marco','cinema',
       'python','xereca','antimonitor')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
