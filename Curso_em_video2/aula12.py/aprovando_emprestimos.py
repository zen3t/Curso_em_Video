
valor_da_casa = float(input('Digite o valor da casa: '))
seu_salario = float(input('Digite o valor do seu salario: '))
ano_para_pagar = int(input('Digite quantos anos: '))


prestacao = valor_da_casa / (ano_para_pagar * 12)
minimo = seu_salario * 30 / 100
print(f'Para pagar uma casa de {valor_da_casa:.2f} em {ano_para_pagar} anos')
print(f'A prestacao serar de: {prestacao:.2f}')
if prestacao <= minimo:
    print('Emprestimo pode ser consecido')
else:
    print('Emprestimo negado')

