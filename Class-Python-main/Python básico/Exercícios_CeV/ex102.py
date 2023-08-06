def fatorial(a,show=0):
    """
    :param a: Número fatorial.
    :param b:   Se Show = True: Mostra a conte.
                Se Show = False: Mostra só o resultado.
    """

    fat = 1
    if show==True:
        print(f'{a}! = ', end = '')
        for c in range(1,a+1):
            fat = fat*c
            if c == a:
                print(c, end ='')
                break
            print(f'{c}x', end = '')
    else:
        for c in range(1,a+1):
            fat = fat*c
        print(f'{a}!', end = '')
    s = f' = {fat} '
    return s

#programa principal
print(fatorial(6,  show = True))

