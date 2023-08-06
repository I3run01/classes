lista = []
c = 0

while True:

    #colocar valores na lista
    lista.append(int(input('Digite número: ')))
    v = lista[:]

    #Verificação de repetição
    if c > 0:
        if v[c] in lista[0:c]:
            print('Número repetido')
            lista.pop()
            c = c-1

    #Verificação de parada
    parada = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    #print(parada)

    if parada == 'N':
        break
    c = c+1
lista.sort()

print(f'A lista em ordem crescente é {lista}')