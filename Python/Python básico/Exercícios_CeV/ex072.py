num = ('um' , 'dois' , 'três', 'quarto','cinco', 'seis',
    'sete', 'oito' , 'nove', 'dez', 'onze', 'doze', 'treze','quartoze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    termo = int(input('Digite o número que você quer ver por extenso entre 1 e 20: '))

    if (termo > 0) and (termo <=20):
        break

print(f'Você digitou o número {num[termo-1]}')