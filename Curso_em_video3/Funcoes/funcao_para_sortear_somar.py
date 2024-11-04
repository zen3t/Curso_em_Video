from random import randint

from time import sleep

def sortear(lista):
    print('Sorteando os 5 valores da lista ',end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        sleep(0.3)
        print(f'{n}',end=' ',flush=True)
    print('Pronto')
def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somandos os valores pares de {lista} temos {soma}',end=' ',flush=True)
    print()

numeros = list()
sortear(numeros)
somaPar(numeros)
