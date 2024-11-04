matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = scol= maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um numero [{l}] [{c}]'))
print('-=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'a soma dos pares é: {par}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'a soma da terceira coluna é: {scol}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior da segunda linha é: {maior}')

