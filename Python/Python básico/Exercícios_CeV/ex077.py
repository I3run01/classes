palavras = ('correr', 'andar', 'dormir')

for p in palavras:
    print(f'\n A palavra {p.upper()} tem as vogais', end=' ')

    for l in p:
        if l in 'aeiou':
            print(l.upper(), end = ' ')
