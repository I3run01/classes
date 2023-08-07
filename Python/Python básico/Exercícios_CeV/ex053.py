frase = str(input('Escreva uma frase: '))
soma=0

frase2 = frase.replace(' ','')
print(frase2)
nl=len(frase2)

for c in range(0,nl):
    if frase2[c]==frase2[nl-c-1]:
        cont=1
    else:
        cont=0
    soma=soma+cont
if soma == nl:
    print('A frase é um polindromo')
else:
    print('A frase não é um polindromo')

