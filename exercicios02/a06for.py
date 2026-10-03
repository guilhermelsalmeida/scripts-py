# for c in range(3): # estrutura de repetição com variável de controle. Pode ser combinado com quase todas as outras estruturas em Python.
  #  print(c)
 #   print('Olá, mundo!')


lista_precos = [1500, 1000, 800, 2000]

taxa_imposto = 0.1 # 10%

for preco in lista_precos:
    imposto = preco * taxa_imposto
    print(f'Valor do produto: R$ {preco:,.2f} | Imposto: R$ {imposto:,.2f}')
    print(f'Valor total: R$ {preco + imposto:,.2f}')

print(' ')


#EXERCÍCIO 01

# for preco in lista_precos:
  #  if preco > 1000:
   #     taxa = 0.15 # 15%
   # else:
    #    taxa = 0.1
   # imposto = taxa * preco
   # print(f'Valor do produto: R$ {preco:,.2f} | Imposto: R$ {imposto:,.2f}')
   # print(f'Valor total: R$ {preco + imposto:,.2f}')

# Muita atenção à endentação.


#EXERCÍCIO 02

# total_imposto = 0
# for preco in lista_precos:
   # if preco > 1000:
    #    taxa = 0.15
   # else:
    #    taxa = 0.1
   # imposto = taxa * preco
   # total_imposto += imposto # total_imposto = total_imposto + imposto
   # print(f'Valor do produto: R$ {preco:,.2f} | Imposto: R$ {imposto:,.2f}')
  #  print(f'Valor do produto com imposto: R$ {preco + imposto:,.2f}')

# print(f'Total de imposto: R$ {total_imposto:,.2f}')


#EXERCÍCIO 03

vendas_23 = {'jan': 15000, 'fev': 10000, 'mar': 5000}
vendas_24 = {'jan': 16000, 'fev': 11000, 'mar': 5100}

# Crescimento percentual: ex: 16000 / 15000 - 1 ou (11000 - 10000) / 10000

for mes in vendas_24: # o Python percorre as chaves do dicionário
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes] # os valores do dicionário são armazenados
    crescimento = valor_24 / valor_23 - 1
    print(f'Mês: {mes} | Cresimento: {crescimento:.1%}')
    print(f'Valor 2023: R$ {valor_23:,.2f} | Valor 2024: R$ {valor_24:,.2f}')