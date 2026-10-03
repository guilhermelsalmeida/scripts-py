# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento: à vista dinheiro/cheque (10% de desconto), à vista no cartão (5% de desconto), em até 2x no cartão (preço formal) ou 3x ou mais no cartão (20% de juros).

print(f'\n{' LOJAS GUILHERME ':=^42}')
preco_compras = float(input('Digite o valor das compras: R$ '))

print('-' * 42)
print(f'''{'FORMAS DE PAGAMENTO':^42}
[ 1 ] À vista no dinheiro, PIX ou cheque
[ 2 ] À vista no cartão
[ 3 ] 2× no cartão
[ 4 ] 3× ou mais no cartão''')
print('-' * 42)

opcao_pagamento = int(input('Escolha a forma de pagamento: '))

if opcao_pagamento == 1:
    preco_final = preco_compras - (preco_compras * 0.1)
elif opcao_pagamento == 2:
    preco_final = preco_compras - (preco_compras * 0.05)
elif opcao_pagamento == 3:
    preco_final = preco_compras
    parcela = preco_final / 2
    print(f'Sua compra será parcelada em 2× de R$ {parcela:.2f}, SEM JUROS.')
elif opcao_pagamento == 4:
    preco_final = preco_compras + (preco_compras * 0.2)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = preco_final / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}× de R$ {parcela:,.2f}, COM JUROS.')
else:
    preco_final = 0
    print('OPÇÃO INVÁLIDA! Tente novamente.')

print(f'Valor final: R$ {preco_final:,.2f}\n')
