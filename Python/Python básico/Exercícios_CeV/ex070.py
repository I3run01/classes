item1 = str(input('Nome do produto: '))
preco1 = float(input('preço do produto: '))
opc1 = str(input('Quer continuar? (S/N)')).strip().upper()[0]
soma = 0
precob = preco1
itemb=item1

#primeira análise de preço
if preco1 > 1000:
    cont = 1
else:
    cont = 0

if opc1 == 'S':
    while True:
        item = str(input('Nome do produto: '))
        preco = float(input('preço do produto: '))
        opc = str(input('Quer continuar? (S/N)')).strip().upper()[0]

        #calculo do preço do produto.
        soma = soma + preco

        #2º analise de preço
        if preco>1000:
            cont = cont +1
        else:
            cont = cont +0

        #Análise do produto mais barato
        if precob<preco:
            precob = precob
            itemb = itemb
        else:
            precob = preco
            itemb = item


        #Opção de parada
        if opc == 'N':
            break

print('')
print(f'O custo da compra = {soma+preco1}')
print(f'Tem {cont} produtos acima de 1000R$')
print(f'O item mais barato é o {itemb} e custa {precob}')
