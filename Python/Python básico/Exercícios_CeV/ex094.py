dados = {}
lmulher = []

c = somaidade = 0

while True:
    dados[f'nome {c}'] = str(input('Nome: '))
    dados[f'sexo {c}'] = str(input('sexo: (Masc/Fem) ')).strip().upper()[0]
    dados[f'idade {c}'] = int(input('idade: '))
    parada = str(input('Deseja continuar: (S/N)')).strip().upper()[0]
    print()

    c = c +1

    if parada == 'N':
        break


print(60*'-')
print(f'Tem cadastradas {c} pessoas')



for cont in range(0,c):
    idade = dados[f'idade {cont}']
    somaidade = idade + somaidade

    if dados[f'sexo {cont}'] == 'F':
        lmulher.append(dados[f'nome {cont}'])

print(60*'-')
print(f'A média das idades = {somaidade/c} ')
print(60*'-')
print(f'Segue a lista das mulheres: {lmulher}')
print(60*'-')
print('Pessoas acima da média: ')
for cont in range(0,c):
    if dados[f'idade {cont}'] > somaidade/c:
        print(f'    -{dados[f"nome {cont}"]} tem {dados[f"idade {cont}"]}')
print(60*'-')





