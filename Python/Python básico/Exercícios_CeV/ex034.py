sal=int(input('Qual o seu salário?'))

if sal>1250:
    print('Seu salario vai aumento 10% \nSeu novo salário é {}'.format(sal*1.10))
else:
    print('Seu salário vai aumentar 15%\nSeu novo salário é {}'. format(sal*1.15))
