def maior(*num):
    tam = len(num)
    vm = 0
    for c in range(0,tam):
        if vm > num[c]:
            vm = vm
        else:
            vm = num[c]

    print(40*'-=')
    print(f'{num}.', end=' ')
    print(f'Foram informados {tam} número,', f' o maior deles é o {vm}')


maior(1, 2, 3)
maior(4,5)
maior(4,6,9,0)


