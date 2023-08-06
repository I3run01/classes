esc=str(input('pedra, papel ou tesoura ?'))

import random
list=['pedra', 'papel', 'tesoura']

escpc=random.choice(list)

print('O computador escolheu {}'.format(escpc))
if (esc=='pedra' and escpc=='pedra') or (esc=='papel' and escpc=='papel') or (esc=='tesoura' and escpc=='tesoura'):
    print('empate')
elif ((esc=='pedra' and escpc=='papel') or (esc=='papel' and escpc==('tesoura')) or (esc=='tesoura' and escpc=='pedra')):
    print('Você perdeu')
else:
    print('Você ganhou')

