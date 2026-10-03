#TUPLAS
def lv():
    print('\n')


# lista_vendas = [1000, 800, 500]
# tupla_vendas = (1000, 800, 500) # tuplas são imutáveis, não podem ser alteradas depois de criadas.
# A principal finalidade da tupla é armazenar dados que não devem ser alterados. Exemplo: dias da semana, meses do ano, resolução de tela, etc.

# print(lista_vendas)
# print(lista_vendas[0])

# print(tupla_vendas)
# print(tupla_vendas[0])
# Ao serem exibidas, o resultado visual é o mesmo, mas a tupla não pode ser alterada, enquanto a lista pode.
# lv()

# lista_vendas[0] = 1200 # se a mesma coisa for feita com a tupla, ocorrerá um erro.
# print(f'Lista vendas atualizada: {lista_vendas}')
# O mais comum é encontrar tuplas em resultados de funções. Exemplo: divmod(), que retorna o quociente e o resto da divisão de dois números, em forma de tupla.
lv()

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

vendas = [100, 250, 400, 1000]
# resultado = calcular_bonus(vendas)

bonus1f, bonus2f = calcular_bonus(vendas) # unpacking da tupla: serve para atribuir os valores da tupla a variáveis separadas. Só funciona com funções que retornam tuplas.
# print(f'Bônus por quantidade de vendas: R$ {resultado[0]:.2f}')
# print(f'Bônus pelo valor total de vendas: R$ {resultado[1]:.2f}')

print(f'Bônus por quantidade de vendas: R$ {bonus1f:.2f}')
print(f'Bônus pelo valor total de vendas: R$ {bonus2f:.2f}')

lv()


# lista_telas = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)] # tupla de tuplas: cada elemento da lista é uma tupla.
# for altura, largura in lista_telas: # unpacking da tupla feito dentro do for.
    # print(f'Resolução: {altura} x {largura}')

tela = (800, 600)
altura, largura = tela # unpacking da tupla simples
print(f'Resolução de tela: {altura} x {largura}')

lv()


#EXERCÌCIO

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

vendas = { # dicionário de listas com as vendas de cada vendedor
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

# 1. Calcular o bônus de cada funcionário.
# 2. Calcular o total de bonus 1 pago aos funcionários.
# 3. Calcular o total de bonus 2 pago aos funcionários.
# 4. Por último,  descobrir se a empresa está gastando mais dinheiro com o bônus 1 ou com o bônus 2.

total_bonus1 = 0
total_bonus2 = 0

for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    total_bonus1 += bonus1
    total_bonus2 += bonus2
    print(f'Vendedor: {vendedor} - Bônus 01: R$ {bonus1:,.2f} | Bonus 02: R$ {bonus2:,.2f}')

print(f'\nTotal bônus 01: R$ {total_bonus1:,.2f}')
print(f'Total bônus 02: R$ {total_bonus2:,.2f}')
print(f'Total gasto com bônus em geral: R$ {total_bonus1 + total_bonus2:,.2f}')

print('\nCONCLUSÃO')
if total_bonus1 > total_bonus2:
    print('A empresa está gastando mais com o bônus 01.')
else:
    print('A empresa está gastando mais com o bônus 02.')

lv()