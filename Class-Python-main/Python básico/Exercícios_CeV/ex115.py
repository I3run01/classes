while True:


    print(15*'-=')
    print('        MENU PRINCIPAL')
    print(30*'-')
    print("""
    \033[1;33m1\033[m - \033[1;34mVer Pessoas\033[m 
    \033[1;33m2\033[m - \033[1;34mCadastrar novas pessoas\033[m
    \033[1;33m3\033[m - \033[1;34mSair do Sistema\033[m
    """)
    print(30*'-')
    while True:
        try:
            opc = int(input('\033[1;33mQual opção: \033[m'))
            break
        except:
            print('Opção inválida. Digite uma opção válida!')

    print(15 * '-=')

    if opc == 3:
        print('Saindo do Sistema')
        break

    if opc == 2:
        print('       NOVA PESSOA')
        print(30 * '-')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        print('Cadastro realizado com sucesso!')

        with open('ex115inf', 'a') as arquivo:
            arquivo.write(f'{nome}\n')
        with open('ex115inf', 'a') as arquivo:
            arquivo.write(f'{idade}anos \n')





    if opc == 1:
        cadsl = []
        print('       LISTA DE PESSOAS')
        print(30 * '-')
        with open('ex115inf','r') as arquivo:
            mensagem = arquivo.readlines()
        tam = len(mensagem)
        for c in range(0,tam, 2):
            tamu = len(mensagem[c])
            print(f'{mensagem[c][0:tamu-1]:<10}', end = ' ')
            print(f'{mensagem[c+1]:>20}', end = '')


