import random

soma=0

r1 = random.randint(0,10)
print(r1)

rj = int(input('Qual número o computador sortiou? '))

while rj != r1:
    print('Você errou. Tente novamente ')
    rj = int(input('Qual número o computador sortiou? '))
    cont=1
    soma=soma+cont
print('Você tentou {} vezes'.format(soma+1))