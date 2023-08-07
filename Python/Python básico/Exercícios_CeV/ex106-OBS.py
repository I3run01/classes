def ajuda(a):
    help(a)


while True:
    com = str(input(f'\033[1:30:45m Ajuda em qual comando? \033[m ')).strip()
    if com[0] in 'Ff':
        break
    ajuda(com)




