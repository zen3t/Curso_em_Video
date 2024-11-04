valores = []

while True:
    valores.append(int(input('Digite os valores: ')))



    res = ' '
    if res not in 'SN':
        res = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print(f'Na lista tem: {len(valores)}')
valores.sort(reverse=True)
print(f'Os valores em ordem decresente sao: {valores}')
if 5 in valores:
    print('O numero 5 esta nos valores .!')
else:
    print('O numero 5 nao esta presente nos valores')
