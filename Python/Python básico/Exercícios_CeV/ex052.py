cont=0
n=int(input('Digie um número: '))

for c in range(2,100):
    if n%c==0:
        s=1
    else:
        s=0
    cont=cont+s
if cont==1:
    print('Número primo')
else:
    print('Número não primo')

