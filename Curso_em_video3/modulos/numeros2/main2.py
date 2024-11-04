import moeda

p = float(input('Digite um preco : R$'))
print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p,True)}')
print(f'O aumento  de 10% e {moeda.aumento(p,10,True)}')
print(f'A diminuicao de 13% e {moeda.diminuir(p,13,True)}')
