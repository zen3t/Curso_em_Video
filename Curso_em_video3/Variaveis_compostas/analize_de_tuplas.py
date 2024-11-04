
numeros = (int(input('Digite um numero: ')),int(input('Digite outro numero: ')),int(input('Digite outro valor: ')),int(input('Digite mais um valor: ')))

# n = 1
while True:
    print(f'Os numeros sao: {numeros}')
    
    print(f'O numero 9 aparece :{numeros.count(9)} vezes')
    


    if 3 in numeros:
        print(f'O numero 3 esta na posicao: {numeros.index(3)}')
    else:
        print('O valor 3 nao aparece em nenhuma posicao')

    print('os numeros pares: ',end='')
    for i in numeros:
        if i % 2 == 0:
            print(f'{i}',end=' ')
            print('\n')
    break
    # n = int(input('\nDigite zero pra sair '))

