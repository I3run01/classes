cbf = ('palmeiras', 'Santos', 'Vasco da gama',
    'Grêmio', 'Flamengo', 'Corinthias',
       'Internacional', 'Cruzeiro', 'São Paulo',
        'Atlético minero', 'Botafogo', 'Fluminense',
    'Coritiba', 'Bahia', 'Goiás', 'Guarani',
       'Sport', 'Portuguesa','Atlético Paranaense',
       'Vitória')

print(f'Os quatros primeiros colocados são: {cbf[0:4]}')

print(f'Os últimos colocados são: {cbf[16:20]}')

print(sorted(cbf))

print('O Sport está na {}ª posição'.format(cbf.index('Sport')+1))