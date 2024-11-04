minhalist = []
maior = 0
menor = 0
for c in range(0,5):
    minhalist.append(int(input(f'Digite um numero {c}: ')))
    if c == 0:
        maior = menor = minhalist[c]
    else:
        if minhalist[c] > maior:
            maior = minhalist[c]
        if minhalist[c] < menor:
            menor = minhalist[c]
print(f'{minhalist}')
print(f'{maior} e o maior')
for i,v in enumerate(minhalist):
    if v == maior:
        print(f'apareceu na posicao{i} ....')
        
print(f'{menor} e o menor')
for i,v in enumerate(minhalist):
    if v == menor:
        print(f'apareceu na posicao {i} ...')
