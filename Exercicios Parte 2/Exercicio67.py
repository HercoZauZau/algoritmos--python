while True:
    num=int(input('Digite um número para ver sua tabuada: '))
    print('-'*30)
    if num<0:
        print('Fim do programa.')
        break
    for tab in range(1,11):
        print(f'{tab:2} * {num} = {tab*num}')
    print('-'*30)
