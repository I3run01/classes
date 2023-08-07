nome = str(input('Nome: '))
media = float(input(f'Média do {nome}: '))

if media <7:
    sit = 'rp'
else:
    sit = 'ap'

dici = {'Nome': nome, 'Média': media, 'Situação': sit}

for k,v in dici.items():
    print(f' {k} é {v}')