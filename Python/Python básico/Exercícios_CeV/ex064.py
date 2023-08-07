num = int(input('Digite um número: '))
num2=num
soma = 0
while num != 999:
    print(num)
    num = int(input('Digite um número: '))
    soma = num + soma
print('A soma dos números digitados = {}'.format(soma-999+num2))