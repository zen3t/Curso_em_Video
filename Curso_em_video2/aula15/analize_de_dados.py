
tot18 = totH = totM = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]'))
    if idade >= 18:
        tot18 += 1 
    if sexo == 'M':
        totH += 1 
    if sexo == 'F' and idade > 20:
        totM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar ...'))
    if resp == 'N':
        break

print('acabou')


