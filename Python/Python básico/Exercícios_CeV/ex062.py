a1 = float(input('Digite o primeiro número da PA: '))
r = float(input('Digite a razão da PA: '))

c=0
print(a1)
while c != 9:
    c = c+1
    a1 = a1+r
    print(a1)
sn = int(input('Você quer colocar mais quantos termos? '))
c = 0

while sn != 0:
    while c != sn:
        c = c + 1
        a1 = a1 + r
        print(a1)
    sn = int(input('Você quer colocar mais quantos termos? '))
    c=0
print('FIM')




