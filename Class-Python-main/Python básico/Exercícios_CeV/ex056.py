soma = 0
soma2 = 0

nomer=str(input('Qual o seu nome?  '))
idader=int(input('Qual o sua idade? '))
sexor=str(input('Qual o seu sexo? (masc/fem)'))

print('')
idader2=idader

for c in range(0,3):
    nome=str(input('Qual o seu nome?  '))
    idade=int(input('Qual o sua idade? '))
    sexo=str(input('Qual o seu sexo? (masc/fem)'))

    print('')

    #Calculo da idade da pessoa mais velha

    if idade>idader:
        nomer=nome
    else:
        nomer=nomer
    #Calculo da idade da mulher mais jovem

    if sexo=='masc':
        print('')
    else:
        if idade<20:
            cont=1
        else:
            cont=0
        soma2=soma2+cont



    soma=soma+idade
media=(soma+idader)/4
print('a média de idade é {}'.format(media))

print('O mais velho se chama {}'.format(nomer))

print('Tem {} mulheres com menos de 20 anos' .format(soma2))