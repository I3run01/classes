vcasa=float(input('Qual o valor da casa ?'))
sal=float(input('Qual o seu salário ?'))
tempo=float(input('Quantos anos vc vai pagar a casa?'))

pres=vcasa/(tempo*12)
print('O valor da prestação é {}'.format(pres))

if sal>=(pres*1.3):
    print('Emprestimo aprovado')
else:
    print('Emprestimo não aprovado')
