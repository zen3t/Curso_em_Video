pessoas = []
dado = []
maior = menor = 0
while True:

    dado.append(str(input('Digite uma pessoas: ')))
    dado.append(int(input('Digite uma pesso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    res = str(input('Quer continuar: S/N ')).strip().upper()[0]
    if res in 'Nn':
        break


# for p in pessoas:
#     if p[1]>= 100:
#  #       print(f'{p[0]} tem o maior pesso')
#         maior += 1
#     elif p[1] <= 70:
# #        print(f'{p[0]} tem o menor pesso')
#         menor += 1
print(f'As pessoas foram {len(pessoas)}')
print(f'{maior}KG Foi o maior pesso de: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ',end='')
    elif p[1] == menor:
        print(f'\nE temos {menor}kg como menor pesso: {p[0]}')

