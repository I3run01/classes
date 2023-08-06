apro = {}
gols = []
s = 0

apro['Jogador'] = str(input('Nome do jogador: '))
apro['Número de partidas'] = int(input('Número de partidas: '))

for c in range(0, apro['Número de partidas']):
    gol = int(input(f'Número de gols na partida {c+1}: '))
    gols.append(gol)
    s = s + gol

apro['Lista de gols '] = gols
apro['Total de gols '] = s

print(60*'-=')
print(apro)
print(60*'-=')
for titulo,resposta in apro.items():
    print(f' -{titulo} tem valor {resposta}')
print(60*'-=')
print(f'O jogador {apro["Jogador"]} jogou {apro["Número de partidas"]} partidas')
for c,v in enumerate(gols):
    print(f'    ==>Na {c+1}º partida ele fez {v}')
print(f'Todal de {s} gols')
print(60*'-=')