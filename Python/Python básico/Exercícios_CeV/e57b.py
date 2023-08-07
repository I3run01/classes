sexo = str(input('Digite seu sexo: (M/F)')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Digite seu sexo: (M/F)')).strip().upper()[0]
print('O sexo escolhido foi o {}' .format(sexo))