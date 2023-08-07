lista = []
cont = 0

while True:
    lista.append(int(input('coloque um valor na lista: ')))
    parada = str(input('Deseja continuar? ')).strip().upper()[0]
    print(parada)

    cont = cont +1
    if parada == 'N':
        break
print('')

print(f'Segue a lista original: \n {lista}')
print('')

print(f'Foram digitados {cont} números! ')
print('')

lista.sort(reverse = True)
print(f'Segue a lista de forma decrescente: \n {lista}')
print('')


if 5 in lista:
    print(f'O valor 5 está na lista na posição {lista.index(5)}!')
else:
    print('O 5 não está na lista!')