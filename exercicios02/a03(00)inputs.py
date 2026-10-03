fat = input('Preencha com o faturamento (apenas números): R$ ') # solicita que o usuário insira alguma informação. Sempre vem como texto
fat = fat.replace('R$', '').replace(',', '.') # replace: substitui o que está entre aspas pelo que está entre parênteses

custo = 600

fat = float(fat) # converte o texto em número. É possível usar o float (decimal) ou o int (inteiro)

lucro = fat - custo
print(f'O lucro foi de R$ {lucro:,.2f}.')

vendas_d1 = float(input('Vendas do dia 01: R$ '))
vendas_d2 = float(input('Vendas do dia 02: R$ '))
# São apenas números e não precisa de tratamento de texto. Então, pode inserir o float direto no input

print(f'Total de vendas: R$ {vendas_d1 + vendas_d2:,.2f}.')