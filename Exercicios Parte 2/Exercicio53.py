frase = str (input ('Digite uma frase: ')).upper ( ).split ( )
junto = ''.join (frase)
inverso = junto[::-1]
print ('O inverso de {} é {}.'.format (junto,inverso))
if junto == inverso:
    print ('Temos um Palíndromo!')
else:
    print ('Não temos um palíndromo!')

# Na vídeo-aula tem outra forma (mais difífil) de resolver.
