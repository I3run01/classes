v1 = int(input('1º Digite um valor:'))
valores = []
valores.append(v1)

vamar = v1
vamer = v1


for cont in range(1,5):

    #Valores que võ para a lista
    valores.append(int(input(f'{cont+1}º Digite um valor:')))

    #fórmulas para a obtenção dos maiores valores
    if valores[cont]>vamar:
        vamar = valores[cont]

    else:
        vamar = vamar


    #Fórmula para os menores valores
    if valores[cont]<vamer:
        vamer = valores[cont]

    else:
        vamer = vamer

print(f'O maior número é o {vamar} e se encontra na posição ', end =' ')
for po in range(0,5):
    if vamar == valores[po]:
        print(f'{po+1}º', end=' ')
print(f'\nO menor número é o {vamer} e se encontra na posição ', end=' ')
for po in range(0,5):
    if vamer == valores[po]:
        print(f'{po+1}º', end=' ')








