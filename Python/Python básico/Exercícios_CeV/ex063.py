num = int(input('Escreva um número (n) inteiro qualquer: '))

c=0

n0 = 0
n1 = 1
n2 = 1
print('Segue abaixo A SEQUÊNCIA FIBONACCI (N) vezes:')
while c != num:
    c=c+1
    n1r=n2
    n2 = n2+n1
    n1 = n1r
    print(n2)



