# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

preco = float(input(f'\n{cores["fundoamareloletrapreta"]} Digite o preço do produto: {cores["limpo"]} R$ '))
preco_desconto = preco - (preco * 0.05)

print(f'\nO produto que custava {cores["vermelho"]}R$ {preco:,.2f}{cores["limpo"]}, com 5% de desconto, passa a custar {cores["verde"]}R$ {preco_desconto:,.2f}{cores["limpo"]}.')
