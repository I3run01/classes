
num=int(input('Escreva um número qualquer: '))

mod = str(input('Você quer converter ele para: binário, octal, hexadecimal? '))

if mod == 'binário':
    print('O valor em binário = {}'.format(bin(num)))

elif mod == 'octal':
    print('O valor escrito em octal == {}' .format(oct(num)))

else:
    print('O valor em hexadecimal é {}' .format(hex(num)))
