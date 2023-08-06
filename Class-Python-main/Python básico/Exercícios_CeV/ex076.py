tupla = ('maça',5, 'banana',2, 'refri',4, 'carne' ,30)

print(40*'-')
print(10*' ','LISTA DE PRODUTOS',10*' ')
print(40*'-')

n = 1
c = 0
while c < 8:
    letras = len(tupla[c])

    print(tupla[c],(30-letras)*'.','R$', f'{tupla[n]:>6}')
    c = c+2
    n = n+2
print(40*'-')
