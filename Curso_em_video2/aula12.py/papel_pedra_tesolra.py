from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opcoes:
[ 0 ] PAPELL
[ 1 ] PEDRA
[ 2 ] TESOURA
      ''')
jogador = int(input('Qual é sua jogada?'))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO')
print('-=' * 11)
print(f'O computador jogou: {itens[computador]}')
print(f'O jogador jogou: {itens[jogador]}')
print('-=' * 11)

if computador == 0: # computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador  Vence!')
    elif jogador == 2:
        print('computador Vence')
    else: print('jogada invalida !')
elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('jogada invalida !')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada invalida !')
