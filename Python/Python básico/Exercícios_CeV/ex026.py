frase=str(input('Digite qualquer frase:')).upper()
frase2 = frase.strip()

print('\033[1:32:40mtemos {} as \033[m \n \033[4:31:64m O primeiro a está na posição {}\033[m \n O útimo a está na posição {}'
      .format(frase2.count('A'), frase2.find('A'), frase2.rfind('A')))

