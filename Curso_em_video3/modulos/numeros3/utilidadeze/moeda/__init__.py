def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def dobro(preco=0,fomato=False):
    res = preco * 2
    return res if not fomato else moeda(res)

def aumento(preco=0,taxa=0, formato=False):
    res = preco + (preco * taxa /100)
    return res if format is False else moeda(res)
def diminuir(preco=0,taxa=0,formato=False):
    res = preco - (preco * taxa /100)
    return res if format is False else moeda(res)
def moeda(preco=0,moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
def resumo(preco=0,taxaa=10,taxar=5):
    print('-='*30)
    print('RESUMO DO VALOR'.center(30))
    print('-='*30)
    print(f'preco analizado: \t{moeda(preco)}')
    print(f'dobro do preco: \t{dobro(preco,True)}')
    print(f'Metade do preco: \t{metade(preco,True)}')
    print(f'{taxaa} de aumento:  \t{aumento(preco,taxaa,True)}')
    print(f'{taxar} de reducao:   \t{diminuir(preco,taxar,True)}')
    print('-='*30)
