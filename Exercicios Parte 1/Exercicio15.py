x=int(input('Quantos dias de uso?'))
y=float(input('Quantos Kilometros percorridos?'))
a=(x*60)+(y*0.15)
print('O custo total pelo aluguer do carro e de {:.1f}R$.'.format(a))
