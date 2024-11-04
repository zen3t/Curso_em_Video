
km = int(input('Digite os km rodados: '))

preco = km * 0.50
if km <= 200:
    print('Igual a 200 ou abaixo de 200 o preco e 0.50 centavos')
    print(f'Voce rodou {km} e vai pagar :{preco}R$ !')
elif km > 200:
    preco = km * 0.45
    print('Acima de 200 o preco e 0.45 centavos')
    print(f'Voce rodou mais de {km} e vai pagar :{preco}R$ !')
else:
    print('Fimmm')
