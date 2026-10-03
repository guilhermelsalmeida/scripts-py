# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

salario = float(input(f'\n{cores["fundobrancoletrapreta"]} Digite o salário do funcionário: {cores["limpo"]} R$ '))
novo_salario = salario * 1.15 # ou salario + (salario * 0.15); ou salario + (salario * 15 / 100).

print(f'\nUm funcionário que ganhava {cores["vermelho"]}R$ {salario:,.2f}{cores["limpo"]}, com 15% de aumento, passa a receber {cores["verde"]}R$ {novo_salario:,.2f}{cores["limpo"]}.')
