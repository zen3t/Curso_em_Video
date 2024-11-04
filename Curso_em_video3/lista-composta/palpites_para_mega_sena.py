from random import randint
from time import sleep

lista = []
jogos = []
print('-='* 20)
print('   JOGA NA MEGA SENA    ')
print('-='* 20)
quan = int(input('Quantas vezes voce quer que eu soteie: '))
tot = 1
while tot <= quan:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1

        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-='*3,f'SORTEANDO {quan} JOGOS', '-='*3)
for i,l in enumerate(jogos):

    print(f'Jogo {i+1}: {l}')
    sleep(1)
