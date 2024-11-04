# galera = [['Julio',15],['thiago',12],['joao',21],['Maris',32]]
# # aqui criamos uma copia
# for p in galera:
#         print(p)

galera = []
dados = []
maior = menor = 0
for c in range(0,3):
    dados.append(str(input('digite o seu nome: ')))
    dados.append(int(input('digite a sua idade: ')))
    galera.append(dados[:])
    dados.clear()
print(f'{galera}')


for p in galera:
    if p[1] >= 20:
        print(f'{p[0]} e maior de  idade')
        maior += 1
    else:
        print(f'{p[0]} e menor de idade')
        menor += 1
print(f'Temos {maior} maior de idade,\n e temos {menor} menor idade')
