import moeda109
valor = int(input('Digite um valor: '))

print(f'A metade de {valor} é {moeda109.metade(valor, True)}')
print(f'O dobro de {valor} é {moeda109.dobro(valor, True)}')
print(f'10% de aumento de {valor} é {moeda109.aumento10(valor, True)}')
print(f'13% de desconto de {valor} é {moeda109.diminuir13(valor, True)}')
