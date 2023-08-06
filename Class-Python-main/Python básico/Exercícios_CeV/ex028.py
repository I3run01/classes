import random

r1 = random.randint(0,5)

print(r1)

c1=int(input('Qual o número entre 0 e 5 o computador chutou?'))

if c1==r1:
    print('Você acertou')
else:
    print('Você errou')