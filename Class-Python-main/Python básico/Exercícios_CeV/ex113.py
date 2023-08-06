def leiaint(a):
    print(f'Você digitou o número {a}')


def leiafloat(a):
    print(f'Você digitou o número {a}')


while True:
    try:
        numint = int(input('Digite um número inteiro: '))
        break
    except:
        print('\033[1;31mNúmero invalido!\033[m')

while True:
    try:
        numfloat = float(input('Digite um número real: '))
        break
    except:
        print('\033[1;31mNúmero invalido!\033[m')

leiaint(numint)
leiafloat(numfloat)




