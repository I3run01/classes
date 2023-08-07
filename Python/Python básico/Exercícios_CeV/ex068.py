import random
cont = 0

while True:
    numpc = random.randint(1,10)
    numjog = int(input('Escreva um número: '))
    opjog = str(input('Escolhar entre par ou impar: ')).strip().upper()[0]
    print('')
    numtot = numpc + numjog
    if numtot %2 == 0:
        optot = 'P'
    else:
        optot = 'I'
    if opjog != optot:
        break
    cont = cont + 1

print('-'*30)
print(f'Você jogou {numjog} e o computador jogou {numpc}. \nVocê ganhou {cont} vezes ')



