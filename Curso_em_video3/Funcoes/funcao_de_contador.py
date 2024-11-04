from time import sleep

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-='*20)
    print(f'Conte de {i} ate {f} pulando de {p} ate {p}')
    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont}',end=' ', flush=True)
            sleep(1)
            cont += p
        print('Fimm')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)

            sleep(1)
            cont -= p
        print('Fimm')
contador(1,10,1)
contador(10,0,2)
print('A gora e sua ves de personalizar a contagem')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini,fim,passo)
