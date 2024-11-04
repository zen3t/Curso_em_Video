from numeros1 import moeda

p = float(input('Digite um preco : R$'))
print(f'A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')
print(f'O aumento  de 10% e {moeda.moeda(moeda.aumento(p,10))}')
print(f'A diminuicao de 13% e {moeda.moeda(moeda.diminuir(p,13))}')
