f = 1100 # número inteiro
c = 600

print('Faturamento: ', f)

nv = 500
print('Novas vendas: ', nv)

f = f + nv
i = 0.15 * f
print('Imposto: ', i)

l = f - c - i

print('Novo faturamento: ', f)
print('Custo: ', c)
print('Lucro: ', l)

m = 'O faturamento da loja foi de R$ 1600.00' # string
print(m)

hl = True # boolean

ml = l / f
print('Margem de lucro: ', ml)

print('Módulo: ', 10 % 3) # módulo

na = int(310 / 12) # int, exibe apenas a parte inteira da divisão
meses = 310 % 12 # resto da divisão
print('Número de anos pagando um imóvel: ', na, ' anos e ', meses, ' meses')

dp = round(189 / 4) # arredondamento para o número inteiro mais próximo
print('Dividsão do pagamento: R$ ', dp)

na2 = 290 // 12 # floor division, parte inteira da divisão
meses2 = 290 % 12
print('Número de anos pagando outro imóvel: ', na2, ' anos e ', meses2, ' meses')


# TIPOS DE VARIÁVEIS
# int - números inteiros
# float - números decimais (reais)
# string - texto (caracteres)
# boolean - verdadeiro ou falso (True [1] ou False [0]), valores booleanos
# Nomes de variáveis que têm mais de uma palavra devem ser separados por underline (ex: novas_vendas) ou por letra maiúscula
# mod (módulo) - %, operador de módulo, retorna o resto da divisão
# Floor division - //, operador de divisão inteira, retorna o quociente da divisão sem a parte decimal