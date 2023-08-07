a1=int(input('Digite o primeiro termo de uma PA: '))
r=int(input('Digite a razão dessa PA: '))

for c in range(a1, (a1+9*r)+1, r):
    print(c)