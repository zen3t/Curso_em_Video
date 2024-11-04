

salario = float(input('Digite o salario: '))


if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'O salario e de {salario} e o novo salario vai ser de {novo:.2f}R$ !')
