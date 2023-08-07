nome=str(input('Escreva o seu nome'))
nomec=(nome.strip())
nom2 = nome.split()
print('primeiro nome é \033[1:33:40m{}\033[m'.format(nom2[0]))

nesp = nomec.count(' ')
nesp1 = nesp
print(' último nome é \033[1:32:40m{}\033[m'.format(nom2[nesp1]))