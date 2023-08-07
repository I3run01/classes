soma = cont = 0
while True:
    num = int(input('Coloque um número inteiro qualquer: '))

    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'A soma = {soma}')
print(f'Foram digitados {cont} números')

