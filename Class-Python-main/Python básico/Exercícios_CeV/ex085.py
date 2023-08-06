lista = [[],[]]

for c in range(0,7):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
        lista[0].sort()
    else:
        lista[1].append(num)
        lista[1].sort()

print('')
print(f'segue a lista dos pares: {lista[0]}')
print('')
print(f'segue a lista dos ímpares: {lista[1]}')