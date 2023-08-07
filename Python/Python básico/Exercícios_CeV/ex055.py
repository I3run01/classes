pesor=float(input('Digite o seu peso: '))
pesor2=pesor

for c in range(0,4):
    peso=float(input('Digite o seu peso: '))
    if peso>=pesor:
        pesor=peso
    else:
        pesor=pesor
    if peso<=pesor2:
        pesor2=peso
    else:
        pesor2=pesor2

print('{}kg é o maior peso' .format(pesor))
print('{}kg é o menor peso' .format(pesor2))


