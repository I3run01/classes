peso=float(input('Qual o seu peso (Kg)?  '))
altura=float(input('Qual a sua altura(m)?'))

imc=peso/(altura**2)

print('Seu imc = {:.2f}'.format(imc))

if imc<18.5:
    print('abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso ideal')
elif imc>=25 and imc<30:
    print('Sobrepeso')
else:
    print('Obesidade mórbida')