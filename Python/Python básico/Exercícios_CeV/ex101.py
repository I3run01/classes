
def voto(nasc):
    import datetime
    anohj = datetime.datetime.now().year
    idade = anohj - nasc
    if idade < 16:
        s = f'Com {idade} anos, o voto é negado'
    elif idade >= 16 and idade < 18:
        s = f'Com {idade} anos, o voto é opcional'
    elif idade >=18 and idade < 65:
        s = f'Com {idade} anos, o voto é obrigaório'
    else:
        s = f'Com {idade} anos, o voto é opcional'
    return s

resp = voto(int(input('Ano de nascimento: ')))

print(resp)
