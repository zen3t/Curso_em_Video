
n = int(input('Digite o termo:'))
ter1 = 0
ter2 = 1
print(f'{ter1} {ter2}',end='-')
cont = 3
while cont <= n:
    ter3 = ter1 + ter2
    
    print(f'{ter3}',end='-')
    ter1 = ter2
    ter2 = ter3
    cont += 1
print('fim')
