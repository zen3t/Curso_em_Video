r = 'S'
while r == 'S':
    sexo = str(input('digite o sexo [M/F]')).upper()

    if sexo == 'M' or sexo == 'F':
        r = False
    else:
        r = str(input(f'voce digitou {sexo} quer continuar [S/N]')).upper()
    print(f'sexo valido {sexo}')
print('fimmm')
