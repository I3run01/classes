import random
import time
import operator

print('valores sorteados: ')


sort = {}

for c in range(0,4):
    jogador = random.randint(1,6)
    sort[f'jogador {c+1}'] = jogador

for k,v in sort.items():
    print(f'    O {k} tirou {v}')
    time.sleep(1)

print(sorted(sort.items()))

print('Ranking dos jogadores: ')
for jogadores, sorteio in sorted(sort.items(), key = operator.itemgetter(1), reverse = True):
    print(f'    {jogadores} sorteou o númeor {sorteio}')
    time.sleep(1)











