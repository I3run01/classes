ex = (input('Digite uma expressão matemática: '))

si = 'va'
pont = 0
lista = []
listav = lista[:]

if '()' in ex:
    si = 'inv'

for car in ex:
    lista.append(car)
tam = len(lista)
print(lista)

for cont in range(0,tam):
    if lista[cont] == '(':
        if ')' in lista[cont:tam]:
            po = lista.index(')')
            lista[po] = '0'
        else:
            si = 'inv'
            break
        lista[cont] = '0'
        print(lista)

for cont in range(0,tam):
    if lista[cont] == ')':
        if '(' in lista[0:cont]:
            po = lista.index('(')
            lista[po] = '0'
        else:
            si = 'inv'
            break
        lista[cont] = '0'
        print(lista)



if si == 'inv':
    print('Equação inválida')
else:
    print('Equação válida')





