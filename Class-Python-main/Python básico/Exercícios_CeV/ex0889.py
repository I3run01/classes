lnota = []
laluno = []
lgeral = []

while True:
    aluno = str(input('nome do aluno: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    parada = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    #lista de notas
    lnota.append(nota1)
    lnota.append(nota2)

    #média dos alunos
    media = (nota1+nota2)/2

    #lista com as informações dos alunos
    laluno.append(lnota[:])
    laluno.append(media)
    laluno.append(aluno)

    #lista com todos os alunos
    lgeral.append(laluno[:])

    #apagar as listas já cadastradas na lista geral
    lnota.clear()
    laluno.clear()

    if parada == 'N':
        break

Nalunos = len(lgeral)


print(30*'-')
print(' No         Nome         Média')

for c in range(0,Nalunos):
    ncara = len(lgeral[c][2])
    print(f'{c:>3}', end= '')
    print(5*' ',f'{lgeral[c][2]:^10}', end='')
    print(f'{lgeral[c][1]:>10}', end='')
    print()
print(30*'-')
while True:
    esca = int(input('De qual aluno você quer ver as notas? (999 interrompe!)'))
    if esca == 999:
        break
    print()
    print(f'As notas de {lgeral[esca][2]} são: {lgeral[esca][0]}')
    print(30 * '-')

