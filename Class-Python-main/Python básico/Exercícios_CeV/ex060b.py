num  = int(input('Escreva um numero: '))

for c in range (num-1,0,-1):
    num=num*c
    print(c)
print(num)