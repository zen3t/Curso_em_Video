times = ('Botafogo','Palmeiras','Fotaleza','Flamengo','Sao paulo','Internacional',
         'Bahia','Cruzeiro','Atletic-MG','Vasco','Criciuma','Gremio','Bragantino','Juventude',
         'Fluminense')
while True:
    print('''
    [ 1 ] Os cincos primeiros
    [ 2 ] Os quatros ultimos
    [ 3 ] A posicao do Vasco
    [ 4 ] Os times em ordem alabeticas
    ''')
    opcao = int(input('Escolha a sua opcao: '))
    if opcao == 1:
        print(f'Os cincos primeiros sao :\n {times[0:5]}')

    elif opcao == 2:
        print(f'Os quatros ultimos sao:\n{times[-4:]}')
    elif opcao == 3:
        print(f'O Vasco esta na posicao: {times.index('Vasco')}')
    elif opcao == 4:
        ordem = sorted(times)
        print(f'Os times em ordem alabeticas sao:\n{ordem}')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if res == 'N':

        break
