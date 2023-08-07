lista = [[],[],[]]

for c in range(0,3):
    for d in range(0,3):
        num = int(input(f'Digite o valor da matriz [{c+1}][{d+1}]:'))
        lista[c].append(num)


for c in range(0,3):
    for d in range(0,3):
        print(f'[{lista[c][d]:^5}] ', end=' ')
    print('')