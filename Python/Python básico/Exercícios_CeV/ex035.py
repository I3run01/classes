import math
a=float(input('Reta 1: '))
b=float(input('Reta 2: '))
c=float(input('Reta 3: '))

if math.fabs(b-c)<a<(a+b):
    if math.fabs(a-c)<b<(a+c):
        if math.fabs(a-b)<c<(a+b):
            print('forma triângulo')
        else:
            print('não forma triângulo')
    else:
        print('não forma triângulo')
else:
    print('não forma triângulo')