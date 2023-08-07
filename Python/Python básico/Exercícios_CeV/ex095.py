listagol = []
apro = {}
cont = 0

while True:
    gols = []
    s = 0

    apro[f'{cont} Jogador'] = str(input('Nome do jogador: '))
    apro[f'{cont} Número de partidas'] = int(input('Número de partidas: '))

    for c in range(0, apro[f'{cont} Número de partidas']):
        gol = int(input(f'Número de gols na partida {c+1}: '))
        gols.append(gol)
        s = s + gol

    listagol.append(gols)
    apro[f'{cont} Lista de gols '] = gols
    apro[f'{cont} Total de gols '] = s
    cont = cont + 1

    parada = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if parada == 'N':
        break

print(60*'-=')
print(f'{"cod":<10}', f'{"nome":^12}', f'{"gols":^15}', f'{"total":>20}')
print(60*'-')
for d in range(0, cont):
    print(f'{d:<10}',f'{apro[f"{d} Jogador"]:^15}',f'{apro[f"{d} Lista de gols "]}', (30-3*len(apro[f"{d} Lista de gols "]))*' ',end ='')
    print(f'{apro[f"{d} Total de gols "]:<20}')

print(60*'-')

cont2 = 0
while True:

    cond = int(input('Mostrar dados de qual jogador? (999 Para encerrar) '))

    if cond == 999:
        break

    if (cond > cont) or (cond < 0):
        print('Dados inválidos, tente novamente!')
        print(60 * '-')
        continue

    print(60 * '-=')
    print(f'-- levantamento jogador {apro[f"{cond} Jogador"]}')
    for t in range(0, len(listagol[cond])):
        print(f'No jogo {t} ele fez {listagol[cond][t]}')

    cont2 = cont2 + 1












