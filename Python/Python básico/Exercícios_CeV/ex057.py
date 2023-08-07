soma = 0

for c in range(0,7):
    idade=int(input('Diga a sua idade: '))
    if idade >= 21:
        cont=1
    else:
        cont=0
    soma=soma+cont
print('{} pessoas são maiores de idade'.format(soma))
print('{} são menores de idade'.format(7-soma))
