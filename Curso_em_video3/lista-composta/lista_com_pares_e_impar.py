


lista = [[],[]]
valor = 0
for c in range(1,7):
    valor = int(input('digite um numero: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Os valores pares{lista[0]}')
print(f'os valores impares{lista[1]}')
