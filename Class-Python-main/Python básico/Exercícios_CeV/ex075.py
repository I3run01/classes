n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))
n4 = int(input('Digite um número:'))

tupla = (n1,n2,n3,n4)

print(f'tem {tupla.count(9)} vezes o número 9')

if 3 in tupla:
    print(f'O 3 aparece na {tupla.index(3)+1}ª posição')
else:
    print('Você não digitou o número 3')

c = 0
for c in range(0,4):
    if tupla[c]%2 ==0:
        print(f'O número {tupla[c]} é par')