ano=int(input('Digite um ano: '))

if ano%4==0:
    print('\033[1:32:40mé bissexto\033[m')
else:
    print('\033[1:31:40mNão é bissexto\033[m')