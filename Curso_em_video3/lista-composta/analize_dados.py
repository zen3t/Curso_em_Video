pessoas = []

while True:
    p = str(input('Digite uma pessoas: '))
    pessoas.append(p)


    res = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if res == 'Nn':
        break
print(f'As pessoas foram: {pessoas}')
