#Valores
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite um valor: '))

#Menu
opc = int(input(('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Digite a opção desejada:''')))

#Pular linha
print('')

#Analise da opção 4
while opc==4:

    v1 = float(input('Digite um valor: '))
    v2 = float(input('Digite um valor: '))

    opc = int(input(('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa

    Digite a opção desejada:''')))

#Analise de uma opção inválida
while (opc !=1) and (opc !=2) and (opc !=3) and (opc !=4) and (opc !=5):
    print('A opção selecionada é invalida. Tente novamente! ')
    v1 = float(input('Digite um valor: '))
    v2 = float(input('Digite um valor: '))

    opc = int(input(('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [5] Sair do programa

    Digite a opção desejada:''')))

#Condicionais das opções 1,2,3
if opc == 1:
    soma = v1+v2
    print('A soma é = {}' .format(soma))
elif opc==2:
    mult= v1*v2
    print('O produto = {}' .format(mult))
elif opc==3:
    if v1>v2:
        print('O maior valor é o {}'.format(v1))
    else:
        print('O maior valor é o {}'.format(v2))
else:
    print('Saindo do programa... ')
