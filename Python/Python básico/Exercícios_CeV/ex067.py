
num = int(input('Digite um valor para ver a tabuada dele: ' ))
print('-'*30)

c = 1

while True:
    while c != 11:
        print(f'{num}x{c} = {num*c}')
        c = c+1
    print('-' * 30)
    num = int(input('Digite um valor para ver a tabuada dele: '))
    print('-' * 30)
    c=0
    if num <0:
        break
print('Tabuada encerrada, volte sempre: ')
print('-'*30)