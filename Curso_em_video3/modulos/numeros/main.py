import moeda

p = float(input('Digite um preco : R$'))
print(f'A metade de {p} e {moeda.metade(p)}')
print(f'O dobro de {p} e {moeda.dobro(p)}')
print(f'O aumento  de 10% e {moeda.aumento(p,10)}')
print(f'A diminuicao de 13% e {moeda.diminuir(p,13)}')
