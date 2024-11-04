
dicionario = {}
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f"Meida de {dicionario['nome']} "))
print(f"O nome e igual: {dicionario['nome']}")
print(f"A media é igual á: {dicionario['media']}")
if dicionario['media'] >= 6:
    print('A situacao e igual a Aprovado')
else:
    print('A situacao e igual a Reprovado')
