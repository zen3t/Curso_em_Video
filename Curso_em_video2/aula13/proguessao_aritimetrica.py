termo = int(input('Digite o primeiro termo: '))
rasao = int(input('Digite a rasao: '))
decimo = termo + (10 -1) * rasao
for c in range(termo,decimo + rasao ,rasao):
    print(c,end=' - ')
print(end='Acabou\n')
