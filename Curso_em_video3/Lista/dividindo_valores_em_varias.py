valores  = []
par = []
impar = []
while True:
    num = (int(input('Digite os valores: ')))
    valores.append(num)


    res = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if res in 'Nn':
        break
print(f'Os valores sao: {valores}')
for i,v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'os numeros pares sao: {par}')
print(f'os numeros impares sao: {impar}')

