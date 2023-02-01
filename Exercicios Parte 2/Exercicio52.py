num=int(input('Digite um número: '))
total=0
for c in range(1,num+1):
    if num%c==0:
        print('\033[33m',end='')
        total+=1
    else:
        print('\033[31m',end='')
    print(c,end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num,total))
if total==2:
    print('E por isso é PRIMO.')
else:
    print('E por isso não é primo.')

