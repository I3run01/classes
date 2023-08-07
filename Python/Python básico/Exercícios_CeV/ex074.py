import random

num = (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))

print(num)

numma = num[0]
numme = num[0]

c = 0

for c in range(0,5):

    if num[c] > numma:
        numma = num[c]
    else:
        numma = numma

    if num[c] < numme:
        numme = num[c]
    else:
        numme = numme

    c = c+1


print(f'O maior número é o {numma}')
print(f'O menor número é o {numme}')
