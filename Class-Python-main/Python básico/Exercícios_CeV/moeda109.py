def moeda(num):
    valor = f'R${num:.2f}'
    nvalor = valor.replace('.', ',')

    return nvalor

def dobro(num, b = 0):
    numdobro = 2 * num

    if b == True:
        numdobro = moeda(numdobro)
    else:
        numdobro = f'{numdobro:.2f}'
    return numdobro


def metade(num, b = 0):
    nummetade = num / 2

    if b == True:
        nummetade = moeda(nummetade)
    else:
        nummetade = f'{nummetade:.2f}'

    return nummetade


def aumento10(num, b = 0):
    numaumento10 = 1.10 * num

    if b == True:
        numaumento10 = moeda(numaumento10)
    else:
        numaumento10 = f'{numaumento10:.2f}'

    return numaumento10


def diminuir13(num, b = 0):

    numdiminuir13 = 0.87 * (num)

    if b == True:
        numdiminuir13 = moeda(numdiminuir13)
    else:
        numdiminuir13 = f'{numdiminuir13:.2f}'

    return numdiminuir13



