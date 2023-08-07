import random
import time

lista = []
lista2 = []
jogos = int(input('Quantos jogos você quer sortear? '))

for nj in range(0, jogos):
    for op in range(0, 6):
        while True:
            sort = random.randint(1, 60)
            if sort not in lista[0:]:
                break
        lista.append(sort)
    lista2.append(lista[:])
    lista.clear()

for nj in range(0, jogos):
    print(lista2[nj])
    time.sleep(1)


