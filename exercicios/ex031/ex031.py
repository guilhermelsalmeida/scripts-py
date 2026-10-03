# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem de ônibus, cobrando R$ 0.50 por km para viagens de até 200km e R$ 0.45 para viagens mais longas.

distancia = float(input('\nQual a distância da viagem em km? '))
print(f'Você está prestes a começar uma viagem de {distancia:.0f}km.')
# if distancia <= 200:
#    preco = distancia * 0.50
# else:
#    preco = distancia * 0.45

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'Preço da passagem: R$ {preco:,.2f}')
