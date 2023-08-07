print('O valor da multa é 7,00R$ por km/h acima do limite ')
v=float(input('Qual velocidade você ultrapassou ?'))

if v>80:
    print('\033[0:31:40mVocê foi multado\033[m \n\033[0:31:40mO valor da multa é =  \033[1:31:40m[m{} \033[m'.format((v-80)*7))
else:
    print('\033[1:32:40mVocê não foi multado\033[m')