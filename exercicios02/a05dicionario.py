lista_produtos = ['ipad', 'iphone', 'airpod']
lista_precos = [7000, 5000, 2000]

dic_produtos = {'ipad': 7000, 'iphone': 5000, 'airpod': 2000} # dicionários permitem associar itens de listas diferentes. São formados por itens compostos de uma chave e um valor associado. As listas continuam valendo.
# Não podem existir dois valores de chaves iguais (por exemplo, não pode haver 2 iphones).


# Pegando um item da lista
produto = 'iphone'
posicao = lista_produtos.index(produto)
preco = lista_precos[posicao]
print(f'O {produto} custa R$ {preco:,.2f}')


# Pegando um item do dicionário
print(f'O ipad custa R$ {dic_produtos['ipad']:,.2f}')

dic_vendas = {'lucas': [1000, 500, 1500], 'joao': [500, 400, 500]} # 2 chaves com uma lista cada e 2 itens dentro do dicionário no total
print(f'Vendas do Lucas: {dic_vendas['lucas']}')


# Adicionar um item; editar um item; e remover um item
dic_produtos['iphone'] = dic_produtos['iphone'] * 1.1 # editando um item
print(f'Lista de produtos atualizada: {dic_produtos}')

dic_produtos['macbook'] = 12000 # adicionando um item
print(f'Lista de produtos com novos produtos: {dic_produtos}')

item_removido = dic_produtos.pop('macbook') # removendo um item
# o item é removido e o preço fica armazendo em item_removido
print(f'O macbook de R$ {item_removido} foi vendido. Lista atualizada: {dic_produtos}')


# Verificar se existe um item no dicionário
print(f'O iphone está disponível: {'iphone' in dic_produtos}')
# print('iphone' in dic_produtos.keys()) # mesma coisa do comando acima. Apenas o .keys foi omitido lá

print(f'Existe algum produto de R$ 2,000.00: {2000 in dic_produtos.values()}') # encontrando um número no dicionário. Se o .values não for inserido, a verificação sempre será feita nas chaves


# Transformando o dicionário em lista
produtos = list(dic_produtos.keys()) # lista apenas das chaves
print(f'Lista de produtos sem preços: {produtos}')

precos = list(dic_produtos.values()) # lista apenas dos númveros
print(f'Lista de produtos só com os preços: {precos}')


# Contagem de itens no dicionário
qtde = len(dic_produtos)
print(f'Total de produtos disponíveis: {qtde}')


# EXERCÍCIO
print(' ')
dic_produtos = {'ipad': 7000, 'iphone': 5000, 'airpod': 2000, 'macbook': 12000}

produto_buscado = input('Digite o nome do produto: ')
produto_buscado = produto_buscado.strip()
produto_buscado = produto_buscado.lower() # strip: remove espaços vazios; lower: tudo em minúscula

if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado] # preço armazenado
    print('PRODUTO ENCONTRADO!')
    print(f'Produto: {produto_buscado} | Preço: R$ {preco:,.2f}')
else:
    print('PRODUTO NÃO ENCONTRADO')

print(' ')