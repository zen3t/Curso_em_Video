

lista = []


while True:
    n = int(input('digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('valor adcionado com sucesso')
    else:
        print('nao pode')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if res == 'N':
        break

lista.sort()
print(f'os numeros sao: {lista}')


