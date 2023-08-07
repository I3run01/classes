din = int(input('Quanto você quer sacar? '))

c50 = c20 = c10 = c1 = 0

#Notas de 50
if din >= 50:
    while True:
        M50 = din - c50
        c50 = c50 + 1
        if M50 % 50 == 0:
            r50 = din - M50
            break
else:
    r50 = din
    M50 = 0

#Notas de 20
if r50 >= 20:
    while True:
        M20 = r50 - c20
        c20 = c20 +1
        if M20 % 20 == 0:
            r20 = din - M50 - M20
            break
else:
    r20 = r50
    M20 = 0


#Notas de 10
if r20 >= 10:
    while True:
        M10 = r20 - c10
        c10 = c10 +1
        if M10 % 10 == 0:
            break
else:
    M10 = 0

M1 = din - M50 - M20 - M10

print(f'Serão {M50/50} notas de 50R$')
print(f'Serão {M20/20} notas de 20R$')
print(f'Serão {M10/10} notas de 10R$')
print(f'Serão {M1} notas de 1R$')