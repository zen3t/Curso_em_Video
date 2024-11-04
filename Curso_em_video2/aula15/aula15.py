
cont = n = s = 0
 
while True:
    n = int(input('digite um numero: '))
    if n == 99:
        break
    cont += 1
    s += n
print(f'a soma vale {s} e o {cont}')
