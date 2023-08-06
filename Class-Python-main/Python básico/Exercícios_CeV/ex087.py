lista = [[],[],[]]

soma = soma3 = 0

ma2 = 0



#criação da matriz
for l in range(0,3):
    for c in range(0,3):
        num = int(input(f'Digite o valor da matriz [{l+1}][{c+1}]:'))

        # soma de todos os pares
        if num % 2 == 0:
            soma = soma + num

        #soma dos valores da segunda coluna
        if c == 2:
            soma3 = num + soma3

        #soma dos valores da primeira linha
        if l == 1:
            if num > ma2:
                ma2 = num
            else:
                ma2 = ma2


        lista[l].append(num)


for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}] ', end=' ')
    print('')

print(f'A soma dos valores pares = {soma} ')
print(f'A soma dos valores da 3º coluna = {soma3}')
print(f'O maior valor da 2ª linha = {ma2}')
