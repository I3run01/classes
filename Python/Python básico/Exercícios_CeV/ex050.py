s=0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n%2==0:
        n=n
        print('Par')
        print('n={}'.format(n))
    else:
        n=0
    s=s+n
print(s)
#print('A soma dos valores pares é {}:' .format(n))