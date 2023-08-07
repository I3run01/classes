def leiaint(a):
    if a.isnumeric():
        s = int(a)
    else:
        while True:
            a = str(input(('Digite um número inteiro: ')))
            if a.isnumeric():
                s = int(a)
                break
    return s




#programa principai
num = str(input('Coloque um número inteiro: '))
resp = leiaint(num)

print(f'Você digitou o número {resp} ')
