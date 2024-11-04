def leiaInter(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERROR! digite um numero inteiro valido: ')
        if ok:
            break
    return valor
n = leiaInter('digite um numero: ')
print(f'voce acabou de digitar um numero {n}')
