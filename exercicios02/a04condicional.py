#  CONDICIONAL - IF

fat = 1_000
custo = 600

lucro = fat - custo

# comparadores: < (menor que), > (maior que), <= (menor ou igual), >= (maior ou igual), == (igual a) e != (diferente de)

if lucro >= 0:
    print(f'Lucro de R$ {lucro:.2f}')
else: # senão
    print(f'Prejuízo de R$ {lucro:.2f}')

# o if pode ser inserido sem else
# o if... else... devem atender à endentação, senão dá erro no código
# é possível colocar if dentro de if
print('=== Faturamento Verificado ===')
print(' ')


# EXEMPLO 01

# produtos = ['iphone', 'ipad', 'airpod']
# novo_produto = input('Digite o nome do produto: ')

# if novo_produto in produtos:
#    print('Produto já existente')
# else:
#    print(f'O {novo_produto} foi cadastrado com sucesso')
#    produtos.append(novo_produto)

# print(f'Produtos disponíveis: {produtos}')


# EXEMPLO 02

# rem = 5_500
# print(f'Remuneração do funcionário: R$ {rem:,.2f}')

# vendas = input('Vendas efetuadas pelo funcionário no mês (somente números): R$ ')
# vendas = vendas.replace('R$', '').replace(',', '.')
# vendas = float(vendas)

# if vendas >= 15000:
#    bonus = 500
# elif vendas >= 5000: # elif: junção do else e do if
#    bonus = 100
# else:
  #  bonus = 0

# print(f'Bônus devido ao funcionário: R$ {bonus:,.2f}')
# print(f'Remuneração do funcionário com bônus: R$ {rem + bonus:,.2f}')


# EXEMPLO 03

rem = 5_500
print(f'Remuneração do funcionário: R$ {rem:,.2f}')

vendas_emp = input('Vendas realizadas pela empresa no mês (apenas números): R$ ')
vendas_emp = vendas_emp.replace('R$', ''). replace(',', '.')
vendas_emp = float(vendas_emp)

meta_emp = 100_000

vendas_func = input('Vendas realizadas pelo funcionário no mês (apenas números): R$ ')
vendas_func = vendas_func.replace('R$', '').replace(',', '.')
vendas_func = float(vendas_func)

if vendas_func >= 15000 and vendas_emp >= meta_emp: # and (e), or (ou)
    bonus = 500
elif vendas_func >= 5000 and vendas_emp >= meta_emp:
    bonus = 100
else:
    bonus = 0

print(f'Bônus devido ao funcionário: R$ {bonus:.2f}')
print(f'Remuneração do funcionário com bônus: R$ {rem + bonus:,.2f}')