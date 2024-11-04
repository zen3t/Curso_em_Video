menu = 1
while menu == True:

    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero:'))
    print('-=='* 30)
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do progama
          ''')
    opcoes = int(input('\033[31mDigite a sua opcoes: \033[m'))
    print('-=='* 30)
    if opcoes == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} = {soma}')
    if opcoes == 2:
        veses = n1 * n2
        print(f'A multiplicacao de {n1} x {n2} = {veses}')
       # menu = False
    if opcoes == 3:
        if n1 > n2 and n2 > n1:
            print(f'Primeiro: {n1} é maior que  o Segundo:{n2}')
        else:
            print(f'Segundo: {n2} é maior que o Primeiro: {n1}')
           # menu = False
    if opcoes == 4:
        print('\033[1;32mNovos numeros \033[m')    
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero:'))

        
        print('''
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos numeros
        [ 5 ] sair do progama
              ''')
        opcoes = int(input('\033[31mDigite a sua opcoes: \033[m'))
        if opcoes == 1:
            soma = n1 + n2
            print(f'A soma de {n1} + {n2} = {soma}')
        if opcoes == 2:
            veses = n1 * n2
            print(f'A multiplicacao de {n1} x {n2} = {veses}')
           # menu = False
        if opcoes == 3:
            if n1 > n2 and n2 > n1:
                print(f'Primeiro: {n1} é maior que  o Segundo:{n2}')
            else:
                print(f'Segundo: {n2} é maior que o Primeiro: {n1}')
           # menu = False
    if opcoes == 5:
        menu = False
