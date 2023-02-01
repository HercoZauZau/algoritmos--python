import random

a = str(input('Aluno 1'))
b = str(input('Aluno 2'))
c = str(input('Aluno 3'))
d = str(input('Aluno 4'))
x = [a, b, c, d]
random.shuffle(x)
print('A ordem de alunos sera', x)
