maior = menor = quant = s = n = 0

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if  n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'A soma dos {quant} valores é: {s} ')
print(f'O maior {maior} e o menor {menor}')
