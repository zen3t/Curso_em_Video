'''
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
a notaram a data da maratona
'''
nome = str(input('Digite uma frase: ')).replace(' ','').upper()
#nome = str(input('Digite uma frase: ').upper()).strip()
palindromo = nome[::-1]
if palindromo == nome:
    print(f'O nome: {palindromo} é palindromo')
else:
    print(f'O nome: {palindromo} nao e palindromo')

