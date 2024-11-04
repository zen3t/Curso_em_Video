from time import sleep
def maior(* num):
    cont = maior = 0
    # num = [8,4,3,5]
    for valor in num:
        print(f'{valor}',end=' ',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores')
    print(f'O maior valor {maior}')
maior(7,4,0,8,2)
