num1=float(input('n1: '))
num2=float(input('n2: '))
num3=float(input('n3: '))

if num1<num2:
    if num1<num3:
        print('{} é o menor número' .format(num1))
    else:
        print('{} é o menor número' .format(num3))
else:
    if num2<num3:
        print('{} é o menor número'.format(num2))
    else:
        print('{} é o menor número'.format(num3))

if num1>num2:
    if num1>num3:
        print('{} é o maior número' .format(num1))
    else:
        print('{} é o maior número' .format(num3))
else:
    if num2>num3:
        print('{} é o maior número'.format(num2))
    else:
        print('{} é o maior número'.format(num3))