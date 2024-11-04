from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))    
    computador = randint(1,10)
    
    total = jogador + computador
    
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar : [P/I]')).upper().strip()[0]    
    print(f'voce jogou {jogador} o computador foi {computador} total de {total}  ')

    if tipo == 'P':
     
        if total %  2 == 0:
            
            print(f' total de {total} .voce venceu deu par',end='\n')
            v += 1
        else:
            print('Voce perdeu ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Voce venceu o total {total}')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente?')
