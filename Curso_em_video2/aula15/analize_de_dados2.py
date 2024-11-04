


total18 = totalH = total20 = 0

while True:
    print('cadrastro de pessoas')
    print('')
    idade = int(input('Idade:'))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        total18 +=1 
    if sexo == 'M':
        totalH += 1 
    if sexo == 'F' and idade < 20:
        total20 += 1 

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'O total de homem com maior de 18 anos foi: {total18}')
print(f'O total de homens no cadrastro foi {totalH}')
print(f'temos {total20} mulheres menores de 20 anos')
