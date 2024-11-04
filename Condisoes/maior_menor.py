n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um  numero: '))

if n1 > n2 and n1 > n3:
    print(f'N1: {n1} e maior {n2} e {n3} ...')

elif n2 > n1 and n2 > n3:
    print(f'N2: {n2} e maior que {n1} e {n3} ....')
else:
    print(f'N3: {n3} e maior ...')
