lista = [0]
valor1 = int(input('Digite um valor: '))
lista.insert(1,valor1)

print('Valor colocado do início da lista!')

for c in range(0,4):
    valor = int(input('Digite um valor: '))
    d = len(lista)
    print(d)
    if valor >= lista[d-1]:
        lista.insert(d, valor)
        print(f'valor colocado na posição {d}')
    else:
        for cont in range(0,d):
            if valor < lista[cont]:
                lista.insert(cont, valor)
                print(f'valor colocado na posição {cont}')
                break

lista.pop(0)
print(lista)



