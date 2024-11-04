


jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    partidas.clear()
    for g in range(0,tot):
        partidas.append(int(input(f"Quantos gols na partida {g+1}º: ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR: responda apenas S ou N')
    if resp == 'N':
        break

print('-='*26)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:>15}',end='')
print()
print('-='*26)
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):>15} ',end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador [999 para parar]?'))
    if busca == 999:
        break
    if busca >= len(time):

        print(f'ERROR: nao existe jogador com esse codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f'  -- no jogo {i+1}º fez {g} gols')
    print('-='* 26)
print('Volte sempre')


