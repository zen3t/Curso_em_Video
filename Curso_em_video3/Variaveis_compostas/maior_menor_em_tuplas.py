from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for i in n:
    print(f'{i}',end=' \n')
print(f'o maior foi {max(n)}')
print(f'o menor foi {min(n)}')
