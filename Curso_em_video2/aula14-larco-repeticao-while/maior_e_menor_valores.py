res = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while res in 'Sn':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:

            maior = num
        if num < menor:
            menor = num
    res = str(input('quer continuar [S/N]')).upper().strip()[0]   
media = soma / quant
print(f'voce digitou {quant} e a media foi: {media}')
print(f'O maior foi: {maior} e o menor foi: {menor}')
