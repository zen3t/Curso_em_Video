 


def area(l,c):
    s = l * c
    print(f'A area de um terreno de {l}x{c} e igual a {s:.2f}')



print('Controle de Terrenos')
print('-='*20)
l = float(input('LARGURA: (M) '))
c = float(input('COMPRIMENTO: (M) '))
area(l,c)
