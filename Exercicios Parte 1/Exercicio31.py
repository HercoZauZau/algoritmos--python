x=int(input('Qual a distancia da sua viagem?'))
if x<=200:
    print('Uma passagem de {}Km custa RS{}'.format(x,x*0.5))
else:
    print('Uma passagem de {}Km custa RS{}'.format(x,x*0.45))
print('BOA VIAGEM :)')
