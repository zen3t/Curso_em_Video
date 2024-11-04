from datetime import date
ano_atual = date.today().year
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = ano_atual - nasc
cadastro['carteira'] = int(input('Carteira de Trabalho (0 nao tem):'))
if cadastro['carteira'] !=0:
    cadastro['contratacao'] = int(input('Ano de Contratacao: '))
    cadastro['salario'] = float(input('Salario R$: '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - ano_atual)
print('-='*20)
for k,v in cadastro.items():
    print(f" - {k} tem o valor {v}")


# print(f" -nome tem o valor de {cadastro['nome']}")
# print(f" -idade tem o valor de {cadastro['idade']}")
# print(f" -ctps tem o valor de {cadastro['carteira']}")
