# Escreva um programa que pergunte a quantidade de quilômetros (km) percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

distancia = float(input('\nDigite a quantidade de quilômetros (km) percorridos: '))
dias = int(input('Digite o total de dias alugados: '))
preco = (dias * 60) + (distancia * 0.15)

print(f'\nUm carro alugado por {dias} dias e percorrendo {distancia:.2f}km, custará R$ {preco:,.2f}.')
