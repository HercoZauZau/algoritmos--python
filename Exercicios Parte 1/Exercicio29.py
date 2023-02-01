x=int(input('Qual a velocidade atual do seu carro em KM/H?'))
print('PROCESSANDO...')
import time
time.sleep(3)
print('A velocidade max. permitida e de 80Km/H. Voce tem uma multa de RS{}.'.format((x-80)*7) if x>80 else 'Voce esta dentro do limite de velocidade. Boa Viagem.')
