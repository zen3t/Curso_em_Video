from datetime import date
ano_atual = date.today().year
somamaior = 0
somamenor = 0
for i in range(1,7):
    a = int(input(f'Digite o {i} ano de nascimento: '))
    idade = ano_atual - a
    if idade >= 18:
        somamaior += 1
    else:
        somamenor += 1

print(f'A soma de maior idade: {somamaior}\nA soma de menor: {somamenor}')
