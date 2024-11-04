from random import randint
from time import sleep
joga = 'S'
cont = 0
soma = 0
print('vou pensar em um numero entre  1 a 10. Tente advinhar')
 

while joga == 'S':
    computado = randint(1,10)   
    jogador = int(input('Em que numero eu pensei: '))
    cont += 1
    if jogador == computado:

        sleep(2)
        print('ANALIZANDO .....')
        print(f'voce precisou jogar {cont} vezes para ganhar\nO numero foi: {jogador}')
        joga = False
    else:
        print(f'O computado jogou o numero: {computado}')
        
print('fimm')
