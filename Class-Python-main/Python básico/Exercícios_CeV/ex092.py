import datetime
data = datetime.datetime.now()

carte = {}

carte['nome'] = str(input('nome: '))
nascimento = int(input('Ano de Nascimento: '))
carte['Número da carteira'] = int(input('Número da carteira de trabalho: (Digite 0 se não tiver) '))
carte['idade'] = data.year - nascimento


if carte['Número da carteira'] != 0:
    carte['ano de contratação'] = int(input('Ano de contratação: '))
    carte['salário'] = float(input('Salário: '))
    carte['Idade de aposentadoria'] = carte['ano de contratação'] + 35-nascimento

print(90*'-')
for titulo, resposta in carte.items():
    print(f'    -{titulo} tem valor de {resposta}')