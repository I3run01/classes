def notas(*a, sit):
    """
     Função para analisar várias notas
     a situação indica as condições em que estão os alunos
     [Boas, Preocupante, Péssimas]
    """

    #Quantidade de notas
    dic = {}
    tam = len(a)
    amax = soma = 0
    amin = -1
    for c in range(0,tam):

        #maior número
        if amax>a[c]:
            amax = amax
        else:
            amax = a[c]

        #menor número
        if amin == -1:
            amin = a[c]
        elif amin != -1 and amin < a[c]:
            amin = amin
        else:
            amin = a[c]

        #Média
        soma = soma + a[c]

    media = soma/tam

    if media >= 7:
        sit = 'BOA'
    elif media > 4 and media <= 7:
        sit = 'Preocupante'
    else:
        sit = 'Péssima'



    dic['notas'] = a
    dic['Quantidade de notas'] = tam
    dic['Maior nota'] = amax
    dic['Menor nota'] = amin
    dic['Média da turma'] = media
    dic['Situação'] = sit

    return dic

#programa principal
resp = notas(10,6,4,1,10, sit = True)
print(resp)

dir(int)