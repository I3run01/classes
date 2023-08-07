cont18 = contm = contf20 = 0

while True:

    #chamada de idade e sexo.
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Qual o seu sexo: (M/F)')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual o seu sexo: (M/F)')).strip().upper()[0]
    print('-'*30)

    #contador de pessoas acima de 18 anos.
    if idade > 18:
        cont18 = cont18 + 1

    #contador de sexo masculino
    if sexo == 'M':
        contm = contm +1
    else:
        contm = contm +0

    #Contador de mulheres com menos de 20 anos.
    if sexo == 'F':
        if idade<20:
            contf20 = contf20 + 1
        else:
            contf20 = contf20 + 0



    #Decisão de continuar ou não.
    cont = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while cont != 'S' and cont != 'N':
        cont = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O número de pessoas acima de 18 anos são: {cont18}')
print(f'O número de homens cadastrados são de: {contm}')
print(f'O número de mulheres com menos de 20 anos são: {contf20}')