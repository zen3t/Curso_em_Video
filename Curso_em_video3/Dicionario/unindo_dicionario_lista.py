pessoa = dict()
turma = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    turma.append(pessoa.copy())
    
    while True:
        res = str(input('Que continuar [S/N]')).strip().upper()[0]
        if res in 'SN':
            break
        print('Erro apenas S ou N')
    if res == 'N':
        break
print(f"A) Ao todo temos {len(turma)} pessoas cadastradas")
media = soma / len(turma)
print(f"B) A media de idade e {media:5.2f} anos")
print('C) As mulheres cadastradas foram: ',end='')
for p in turma:
    if p['sexo'] in 'Ff':
        print(f'[{p["nome"]}]',end=',')
print()
print('D) Lista das pessoas que estao acima da media')
for p in turma:
    if p['idade'] >= media:
        print('    ',end='')
        for k,v in p.items():
            print(f'{k} = {v} ',end=' ')
        print()
