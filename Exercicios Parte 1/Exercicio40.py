x=float(input('Digite sua primeira nota:'))
y=float(input('Digite sua segunda nota:'))
z=(x+y)/2
if z<5:
    print('Média {:.1f} \033[31mREPROVADO\033[m'.format(z))
if z>=5 and z<=6.9:
    print('Média {:.1f} \033[33mRECUPERAÇAO\033[m'.format(z))
if z>=7:
        print('Média {:.1f} \033[32mAPROVADO\033[m'.format(z))
