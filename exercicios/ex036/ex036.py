# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa deve perguntar o valor da casa, o salário do comprador e em quantos anos vai pagar. Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou o empréstimo será negado.

casa = float(input('\nDigite o valor da casa: R$ '))
salario = float(input('Digite o valor do salário: R$ '))
anos = int(input('Digite em quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)
valor_maximo = salario * 0.3

if prestacao <= valor_maximo:
    print(f'\nFinanciamento aprovado! O valor da prestação será de R$ {prestacao:,.2f} por mês.\n')
else:
    print(f'\nFinanciamento negado. O valor da prestação de R$ {prestacao:,.2f} excede o teto de 30% do salário.\n')
