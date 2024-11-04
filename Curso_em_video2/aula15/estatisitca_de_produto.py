gasto = menor = total = cont  = 0
barato = ' '
while True:
    preco = int(input('Digite os precos dos produtos: '))
    nome = str(input('Digite o nome do produto: '))
    gasto += preco
    cont += 1 
    if preco > 1000:
        
        total += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).upper().strip()[0]

    if resp == 'N':
        break
print(f'O total gasto {gasto}\nO produto mais barato é: {barato} que custa: {menor}')
print(f'{total} maiores de 1000')
