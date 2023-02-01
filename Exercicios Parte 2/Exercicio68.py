from random import randint
cont=0

print('\033[1;30;44mPAR OU ÍMPAR\033[m')
while True:
    pc=randint(1,10)
    user=int(input('Diga um valor: '))
    num=input('Par ou Ímpar [P/I]: ').strip().upper()[0]
    if num not in 'PI':
        while True:
            num=input('Par ou Ímpar [P/I]: ').strip().upper()[0]
            if num in 'PI':
                break
    result=pc+user
    if result%2==0 and num=='P':
        print(f'Você jogou {user} e o computador jogou {pc}. Total de {result} : PAR')
        cont+=1
    if result%2!=0 and num=='I':
        print(f'Vocè jogou {user} e o computador jogou {pc}. Total de {result} : IMPAR')
        cont+=1
    if result%2==0 and num=='I':
        print(f'Você jogou {user} e o computador jogou {pc}. Total de {result} : PAR')
        print('Você perdeu!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
    if result%2!=0 and num=='P':
        print(f'Você jogou {user} e o computador jogou {pc}. Total de {result} : IMPAR')
        print('Você perdeu!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
