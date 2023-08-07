
num = int(input('Digite um valor: '))
num2=num
soma  = 0
cont = 0
cp = ''
while cp != 'S':
    num = int(input('Digite outro valor: '))
    numma = num
    numme = num
    cp = str(input('Você quer encerrar? (Sim/Não)')).strip().upper()[0]
    soma = soma + num
    cont = cont + 1
    if num2>numma:
        numma=num2
    else:
        numma=numma
    if num2<numme:
        numme=num2
    else:
        numme=numme

media = (soma+num2)/(cont+1)
print('A média = {}' .format(media))
print('O maior valor é {}'.format(numma))
print('O menor valor é {}' .format(numme))



