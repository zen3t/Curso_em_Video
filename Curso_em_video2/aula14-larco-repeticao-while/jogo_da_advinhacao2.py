from random import randint
computador = randint(0,10)
print('Sou seu computador acabei de pensar em um numero de 0 a 10')
print('Será que voce consegue advinhar qual foi !')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite o seu numero: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais .... Tente mais uma vez ....')
        else:
            print('Menos .... Tente mais uma vez ...')

print(f'O jogador acertou com {palpite} tentativas .')

