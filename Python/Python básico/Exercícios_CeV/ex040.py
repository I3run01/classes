n1=float(input('Nota 1:'))
n2=float(input('Nota 2 :'))

m=(n1+n2)/2
print(m)

if m<5:
    print('Reprovado!')
elif 5<=m<=6.9:
    print('Recuperação')
else:
    print('aprovado')