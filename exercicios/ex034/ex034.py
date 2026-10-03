# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('\nDigite o salário do funcionário: R$ '))

if salario > 1250:
    novo_salario = salario * 1.10
else:
    novo_salario = salario + (salario * 15 / 100)

print(f'Salário anterior: R$ {salario:,.2f}')
print(f'Novo salário com aumento: R$ {novo_salario:,.2f}\n')
