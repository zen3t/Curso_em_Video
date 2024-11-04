primeiro = int(input('digite o primeiro termo: '))
rasao = int(input('digite a rasao:'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -',end='')
    termo += rasao
    cont += 1
print('fimm')

