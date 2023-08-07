import random

a1=str(input('aluno 1'))
a2=str(input('aluno 2'))
a3=str(input('aluno 3'))
a4=str(input('aluno 4'))

list=[a1, a2, a3, a4]
random.shuffle(list)

print('a ordem é {}'.format(list))
