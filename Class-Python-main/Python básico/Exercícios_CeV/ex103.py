def ficha(a, gols ):
    gols = str(input('gols: '))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if a == '':
        a = '<desconhecido>'
    print(f'O jogador {a} fez {gols} gols!')

#programa principal
jogador = str(input('Jogador: '))
ficha(jogador, gols = 0)

