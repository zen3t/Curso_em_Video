lista = []
impar = []
par = []
for i in range(0,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        par.append(n) 
    elif n % 2 == 1:
        impar.append(n)
lista.append(par)
lista.append(impar)
lista.sort()
print(f'Os numero pares: {lista[0]}')
print(f'Os numero impares: {lista[1]}')

