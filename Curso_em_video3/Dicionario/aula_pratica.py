'''pessoas = {'nome':'joao','idade':43,'sexo':'M','altura':1.75}
# print(f"O {pessoas['nome']} tem {pessoas['idade']}")
del(pessoas['sexo'])
# isso apaga um item do dicionario
pessoas['nome'] = 'zeneto'
# Isso modifica o novo nome no dicionario
pessoas['peso'] = 98.78
# Com isso adciona o novo items no dicionario
for k in pessoas.keys():
    print(k)
# Mostra as chaves que sao nome, idade,sexo, altura
print(pessoas.values())
# Mostra os valores que sao joao, 43, M, 1.75
for k,v in pessoas.items():
    print(f"{k} = {v}")
# Mostra todos os itens do dicionario

brasil = []
estado1 = {'uf':'Rio de janeiro','sigla':'Rj'}
estado2 = {'uf':'Sao paulo','sigla':'Sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])
print(brasil[1]['uf'])

'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Digite a unidade federativa: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    brasil.append(estado.copy())
    for e in brasil:
        for k,v in e.items():

            print(f'O campo {k} tem valor {v}')
        print()
