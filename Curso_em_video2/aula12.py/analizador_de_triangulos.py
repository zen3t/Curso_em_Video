
reta_a = float(input('Digite um tamanho : '))
reta_b = float(input('Digite outro tamanho : '))
reta_c = float(input('Digite mais um tamanho : '))

if(reta_a + reta_b > reta_c) and (reta_a + reta_c > reta_b) and (reta_b + reta_c > reta_a):
    print('Os seguimentos acima PODEM FORMA um triangulo')


    if reta_a == reta_b == reta_c : 
        print(f'Forma um triangulo Equilatero')

    elif (reta_a != reta_b) and (reta_a != reta_c) and (reta_b != reta_c):
         print('forma um triangulo ESCALENO')
    elif (reta_a + reta_b > reta_c) and (reta_a + reta_c > reta_b) and (reta_b + reta_c > reta_a):
        print(f'forma um ISOSCELES')
else:
    print(' nao forma um triangulo')

