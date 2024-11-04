lista = ('banana',2.75,'melancia',3.90,'uva',4.90)

for pos in range(0,len(lista)):
    if pos % 2 == 0:

        print(f'{lista[pos]:.<30} ',end='')
    else:
        print(f'R$:{lista[pos]:>7.2f}')
