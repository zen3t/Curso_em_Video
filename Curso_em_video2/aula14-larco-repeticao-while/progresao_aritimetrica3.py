primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print(f'{termo}',end=' - ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer conectar a mais: '))
print('Fimmm')
