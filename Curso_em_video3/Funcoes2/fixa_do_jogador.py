def ficha(jog='desconhecido',gol=0):
    print(f'O jogador fez {jog} fez {gol} no campeonato')
n = str(input('digite o nome do jogador: '))
g = str(input('digite o numero de gols: '))

if g.isnumeric():
    g = int(g)

else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
