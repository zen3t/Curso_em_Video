n1 = int(input('Informe um numero:'))
n2 = int(input('Informe outro numero:'))

opcao = 0
while opcao != 5:
    print('''
          [1] SOMA
          [2] MULTIPLICACAO
          [3] MAIOR
          [4] NOVOS NUMEROS
          [5] SAIR DO PROGAMA ''')
    print('-=='*20)
    opcao = int(input('Digite a sua opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de: {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplica = n1 * n2
        print(f'A multiplicacao de: {n1} x {n2} = {multiplica}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O primeiro numero é {n1} maior ..')
        else:
            print(f'O segundo numero é {n2} maior ..')
    elif opcao == 4:
        n1 = int(input('Informe um numero:'))
        n2 = int(input('Informe outro numero:'))
    elif opcao == 5:
        print('Finalizando ...')
    else:
        print('Informe forme um opcao valida ...!')
    
print('fimm')
    
