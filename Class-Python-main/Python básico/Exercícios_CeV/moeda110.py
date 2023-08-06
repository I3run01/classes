def moeda(num):
    valor = f'R${num:.2f}'
    nvalor = valor.replace('.', ',')
    return nvalor

def dobro(num):
    numdobro = 2 * num
    numdobro = moeda(numdobro)
    return numdobro


def metade(num):
    nummetade = num / 2
    nummetade = moeda(nummetade)
    return nummetade


def aumento(num, taxa , taxa2):
    numaumento10 = (1+(taxa2/100)) * num
    numaumento10 = moeda(numaumento10)
    return numaumento10


def diminuir(num, taxa, taxa2):
    numdiminuir13 = (1-(taxa/100)) * (num)
    numdiminuir13 = moeda(numdiminuir13)
    return numdiminuir13

def resumo(num, taxa, taxa2):
    e = moeda(num)
    a = dobro(num)
    b = metade(num)
    c = aumento(num, taxa, taxa2)
    d = diminuir(num, taxa, taxa2)

    print(29*'-')
    print('       RESUMO DO VALOR')
    print(29 * '-')
    print(f'{"Preço analisado:":<6}', f'{e:>12}')
    print(f'{"Dobro do preço :":<6}', f'{a:>12}')
    print(f'{"Metade do preço:":<6}',f'{b:>12}')
    print(f'{f"{taxa2}% de aumento :":<6}', f'{c:>12}')
    print(f'{f"{taxa}% a menos    :":<6}',f'{d:>12}')




