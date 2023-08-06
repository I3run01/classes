import moeda
valor = int(input('Digite um valor: '))

print(f'A metade de {valor} é {moeda.metade(valor):.2f}')
print(f'O dobro de {valor} é {moeda.dobro(valor):.2f}')
print(f'10% de aumento de {valor} é {moeda.aumento10(valor):.2f}')
print(f'13% de desconto de {valor} é {moeda.diminuir13(valor):.2f}')
