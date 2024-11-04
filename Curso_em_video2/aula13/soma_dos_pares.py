s = 0
cont = 0
print('-'*19)
for i in range(1,7):
    num = int(input(f'Digite o {i} numero: '))
    if num % 2 == 0:
        s = s + num
        cont += 1
print('-'*19)

print('='*32)
print(f'Voce informou {cont} numeros pares e a soma dos numeros pares é: {s}')
print('='*32)
