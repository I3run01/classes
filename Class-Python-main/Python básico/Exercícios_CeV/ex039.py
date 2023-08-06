idade=int(input('Qual a sua idade? '))

if idade<18:
    print('Você vai ter que se alistar daqui {} ano(s)' .format(18-idade))
elif idade==18:
    print('É hora de você se alistar')
else:
    print('Você está {} anos atrasado' .format(idade-18))
