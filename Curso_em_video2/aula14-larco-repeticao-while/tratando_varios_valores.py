num = soma = cont = 0
num = int(input('Digitte um [999 numero para parar: '))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digitte um [999 numero para parar: '))
print(f'voce digitou {cont} e a soma foi {soma}')


