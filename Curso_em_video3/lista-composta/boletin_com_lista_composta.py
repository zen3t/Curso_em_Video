
lista = []
while True:
    nome  = str(input('Digite um nome: '))
    nota1 = float(input('Digite uma nota: '))
    nota2 = float(input('Digite outra nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2], media])

    res = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if res in 'Nn':
        break
print('-='*26)
print(f'{"No.":4<} {"NOME":<10}{"MEDIA":>8}')
print('-='*26)
for i,a in enumerate(lista):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
