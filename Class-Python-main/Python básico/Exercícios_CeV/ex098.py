import time

def contador(a,b, passo):
    va = a

    while True:
        if passo <0:
            passo = passo*(-1)

        elif passo == 0:
            passo = 1

        if b<a:
            print(va, end=' ')
            va = va - passo
            if va <= b:
                break
        else:
            print(va, end=' ')
            va = va + passo
            if va >= b:
                break

        time.sleep(1)

print(60*'-')
contador(1,11,1)
print()
print(60*'-')
contador(10, -2, 2)
print()
print(60*'-')
contador(int(input('valor inicial: ')), int(input('valor final: '))+1, int(input('passo: ')))
