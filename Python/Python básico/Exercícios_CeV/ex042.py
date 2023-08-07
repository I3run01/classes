import math
a=float(input('Reta 1: '))
b=float(input('Reta 2: '))
c=float(input('Reta 3: '))

if math.fabs(b-c)<a<(b+c) and math.fabs(a-c)<b<(a+c) and math.fabs(a-b)<c<(a+b):
    print('formam triângulo')

    if a == b == c:
        print('triângulo equilatero')
    elif a == b or a == c or b == c:
        print('triângulo isosceles')
    else:
        print('Todos os lados diferentes')
else:
    print('Não formam triândulo')

