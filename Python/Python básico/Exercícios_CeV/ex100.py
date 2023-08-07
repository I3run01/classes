def sorteio(lsort):
    import random
    import time
    tam = len(lsort)
    print(30*'-=')
    for c in range(0, tam):
        lsort[c] = random.randint(0,9)
        print(lsort[c], end =' ')
        time.sleep(1)
    print()
    print(30*'-=')

def somapar(list):
    spar = 0
    pares = []
    tam = len(list)
    for c in range(0, tam):
        if list[c] % 2 == 0:
            pares.append(list[c])
            spar = spar + list[c]
    print(f'Foram sorteados {tam} valores: {list} \nSendo a soma dos pares = {spar}')

lista = [0,0,0,0,0]
sorteio(lista)
somapar(lista)
