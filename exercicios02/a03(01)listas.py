print('LOJA DA APPLE')
# LISTAS
# Lembrando que strings são listas de caracteres

lista_vendas = [100, 50, 1000, 800, 35] # listas ficam entre couchetes; pode haver textos e números mesclados, mas não se recomenda misturar valores
# Lembrando que os itens das listas recebem índices numéricos, que começam em 0 (0, 1, 2, 3, 4, ...)

print(f'Segunda venda: R$ {lista_vendas[1]:.2f}') # os couchetes exibem o item de lista correspondente ao índice informado. Nesse caso, será exibido o segudo item da lista
print(f'Penúltima venda: R$ {lista_vendas[-2]:.2f}') # os itens da lista podem ser contados de trás para frente, usando índices negativos (... -4, -3, -2, -1). Nesse caso, será exibido o penúltimo (ou quarto) item

total_itensv = len(lista_vendas)
print(f'Total de vendas realizadas: {total_itensv}') # len (length, tamanho, comprimento) exibe a quantidade de itens na lista

total_v = sum(lista_vendas) # sum (soma) exibe a soma de todos os itens da lista
print(f'Total em vendas: R$ {total_v:.2f}')


# [100, 50, 1000, 800, 35]
print(f'Maior venda realizada: R$ {max(lista_vendas):.2f}') # max: retorna o maior valor da lista

print(f'Menor venda realizada: R$ {min(lista_vendas):.2f}') # min: retorna o menor valor da lista

print(f'Média de vendas: R$ {total_v / total_itensv:.2f}') # não existe uma função de média no python, mas tirar a média é bem fácil


# ENCONTRAR UM ELEMENTO EM UMA LISTA
# lista_vendas = [100, 50, 1000, 800, 35]

lista_produtos = ['iphone', 'ipad', 'apple watch', 'airpod', 'macbook']

print(f'Existem Airpods em estoque? {'airpod' in lista_produtos}') # in: verifica se um item existe em uma lista. Retorna True ou False. É mais usado em listas de produtos. A escrida da lista deve ser igual à escrita da procura.

posicao = lista_produtos.index('airpod') # index: retorna o índice do item na lista.
print(f'Os Airpods estão no setor {posicao} do estoque.')

pedaco_lista = lista_produtos[posicao:] # retorna do item referido até o final da lista.
print(f'Últimos produtos em estoque: {pedaco_lista}')


# EDITAR ITENS EM UMA LISTA

lista_precos = [5_000, 7_000, 3_000, 1_000, 10_000]
print(f'Lista de preços: {lista_precos}')

novo_preco = lista_precos[0] * 1.1
lista_precos[0] = novo_preco
print(f'Lista de preços atualizada: {lista_precos}')

# ['iphone', 'ipad', 'apple watch', 'airpod', 'macbook']

# lista_produtos.remove('macbook') # edita a lista original através da indicação do nome do item ('Macbook'). Então, a variável não precisa ser atualizada.
# print(f'Macbook vendido. Itens restantes: {lista_produtos}')

item_removido = lista_produtos.pop(-1) # remove um item da lista pelo índice numérico (nesse caso, 4 ou -1).
print(f'O {item_removido} foi vendido. Produtos disponíveis: {lista_produtos}')

lista_produtos.append('macbook') # adiciona um item no final da lista, mesmo que já exista (listas podem ter itens duplicados no Python)
print(f'O {item_removido} chegou. Lista atualizada: {lista_produtos}')

lista2_produtos = ['PC', 'air tag', 'caixa de som JBL']
lista_produtos.extend(lista2_produtos) # extende, aumenta, a lista, adicionado os itens da nova lista
print(f'Novos produtos que chegaram à loja: {lista_produtos}')

lista_produtos.insert(1, 'airpod max') # insere um item à lista. Pede o índice em que se pretende colocar o novo item e o nome do novo item. Os itens que vêm depois são deslocados uma posição para a direita
print(f'O airpod max chegou. Lista aualizada: {lista_produtos}')

print(f'Airpods em estoque: {lista_produtos.count('airpod')}') # conta quantas vezes um item aparece na lista

lista_produtos.sort() # sort (ordenar): ordena uma lista em ordem crescente, se números, ou em ordem alfabética, se letras. Usa a ordem da tablea ASCII, na qual todas as maiúsculas vêm antes de todas as minúsculas
print(f'Lista de produtos em ordem alfabética: {lista_produtos}')

lista_precos.sort(reverse=True) # coloca os itens em ordem decrescente. Por padrão vem como False, caso não seja escrito nada.
print(f'Lista de preços em ordem decrescente: {lista_precos}')


# É possível associar uma lista à outra para que, ao reordenar uma lista, a outra não perca seu item correspondente, mas isso será visto em próximas aulas