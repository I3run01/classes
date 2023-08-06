import moeda
valor = float(input('Digite um valor: '))

print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'10% de aumento de {moeda.moeda(valor)} é {moeda.moeda(moeda.aumento10(valor))}')
print(f'13% de desconto de {moeda.moeda(valor)} é {moeda.moeda(moeda.diminuir13(valor))}')
