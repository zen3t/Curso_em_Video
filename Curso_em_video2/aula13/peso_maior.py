pesmaior = 0
pesmenor = 0
for p in range(1,6):
    peso = float(input(f"digite o {p} peso: "))
    if peso == 1:
        pesmaior = peso
        pesmenor = peso
    else:
        if peso > pesmaior:
            pesmaior = peso
        if peso < pesmenor:
            pesmenor = peso

print(f'O maior peso lido foi: {pesmaior}')
print(f'O menor peso lido foi: {pesmenor}')
