
import random

joga = int(input('jogador digite um numero : '))
pc = random.randint(0,5)
if joga == pc:
    print(f'O numero foi {pc} voce ganhou')
else:
    print(f'o numero foi {pc} voce perdeu')
