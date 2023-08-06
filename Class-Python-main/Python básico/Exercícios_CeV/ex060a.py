num = int(input('Escreva um número: '))
num0 = num
numb=num

k = ''

while k != 1:
    k = num - 1
    num = k
    num0=num0*num

print('{}! = {} '.format(numb,num0))
