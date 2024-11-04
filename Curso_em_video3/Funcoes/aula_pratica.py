# criando funcoes
'''
zf = cria uma dobra
zc = fecha uma dobra
zo = abre uma dobra
zR = abre todas as dobras
zM = fecha todas as dobras
def mensagens(msg):
    print('-='*20)
    print(msg)
    print('-='*20)

mensagens('OLA MUNDO')

def soma(a,b):
    print(f'A ={a} B= {b}')
    s = a + b
    print(f'A soma de {a} + {b} = {s}')

soma(2,5)

'''
# criando o contador
# def contador(*num):
#     for i in num:
#         print(i, end='')
#     print()
#
#
# contador(2,4,5,6,8)
# contador(5,6,8)
# contador(2,4,8)
# Passando parametros
# def dobra(lst):
#     pos = 0
#
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
# lista = [12,3,4,6,7]
# dobra(lista)
# print(lista)


def maior(* valores):
    for i in valores:
        max(i)
        print(f'A somando os {i} ')

maior(2,4,5)
