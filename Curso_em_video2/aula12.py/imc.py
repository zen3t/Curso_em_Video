altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura ** 2)
    
print(f'A sua altura é {altura}m seu peso é {peso}kg ')
if imc <= 18.5:

    print(f'Seu imc é: {imc:.1f} Abaixo do peso !')
elif imc >= 18.5 and imc <= 25:
    print(f'{imc:.1f} Peso normal .!')
elif imc >=25 and imc <=30:
    print(f'{imc:.1f} Voce esta Sobrepeso .!')
elif imc >=30 and imc <=40:
    print(f'{imc:.1f} Voce esta com Obesidade  .!')
else:
    print(f'{imc:.1f} Voce esta com Obesidade Morbida .!')

 
