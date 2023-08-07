idade=int(input('Qual a sua idade? '))

if idade<=9:
    print('Mirim')
elif 9<idade<=14:
    print('Infantil')
elif 14<idade<=19:
    print('Junior')
else:
    print('Master')