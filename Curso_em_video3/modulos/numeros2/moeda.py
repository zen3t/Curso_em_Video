def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def dobro(preco=0,fomato=False):
    res = preco * 2
    return res if fomato is False else moeda(res)

def aumento(preco=0,taxa=0, formato=False):
    res = preco + (preco * taxa /100)
    return res if format is False else moeda(res)
def diminuir(preco=0,taxa=0,formato=False):
    res = preco - (preco * taxa /100)
    return res if format is False else moeda(res)
def moeda(preco=0,moeda='R$',fomato=False):
    return f'{moeda}{preco:.2f}'.replace('.',',')
