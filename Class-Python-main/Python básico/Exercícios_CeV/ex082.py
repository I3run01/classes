lista = []
listapar = []
listaimpar = []

while True:
    valor = int(input('Digite um valor: '))
    parada = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    lista.append(valor)

    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)

    if parada == 'N':
        break

print('')
print(f'Lista: {lista}')
print('')
print(f'lista dos números pares: {listapar}')
print('')
print(f'lista dos números impares: {listaimpar}')


