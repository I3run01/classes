valor=float(input('Qual o preço do seu produto? '))
pag=float(input('Qual a forma de pagamento? \n(1) A vita ou cheque \n(2) A vista no cartão \n(3) Em até 2 vezes no cartão \n(4) 3x ou mais no cartão\nDigite aqui: '))

if pag==1:
    print('Desconto de 10%.\nValor = {}' .format(valor*0.90))
elif pag==2:
    print('Desconto de 5%.\nValor = {}' .format(valor*0.95))
elif(pag==3):
    print('Preço normal.\nValor = {}'.format(valor))
else:
    print('acréscimo de 20%.\nValor a pargar = {}'.format(valor*1.20))

