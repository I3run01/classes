#primeira entrada de dados
dados = []
dados.append(str(input('Nome: ')))
dados.append(str(input('peso: ')))

#primeiro termo da lista de pessoas
pessoas = []
pessoas.append(dados[:])
dados.clear()

#listas com os pesos pesados e leves
listape=[]
listalev=[]

#Contador para o While
cont = 0

#Peso máximo e mínimo do primeiro cadastro para comparação
pesoma = pesomi = pessoas[0][1]

#Criação da lista pessoas
while True:
    parada = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if parada == 'N':
        break
    dados.append(str(input('Nome: ')))
    dados.append(str(input('peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    cont = cont + 1

#Criério de comparação para obter o maior peso
for d in pessoas:
    if d[1]>pesoma:
        pesoma = d[1]
    else:
        pesoma = pesoma

#Critério para obter o menor peso
for d in pessoas:
    if d[1]<pesomi:
        pesomi = d[1]
    else:
        pesomi = pesomi


#print do total de pessoas cadastradas
print('')
print(f'O número total de pessoas cadastradas são de {cont+1}')
print('')

#criação da lista com as pessoas mais pesadasn

for d in pessoas:
    if d[1] == pesoma:
        listape.append(d)

#criação da lista com as pessoas mais leves
for d in pessoas:
    if d[1] == pesomi:
        listalev.append(d)

#prints com as listas das pessoas mais pesadas e mais leves
print(f'As pessoas mais pesadas são: {listape}')
print('')
print(f'As pessoas mais leves são: {listalev}')
print('')

