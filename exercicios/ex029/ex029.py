# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado. A multa vai custar R$ 7.00 por cada Km acima do limite.

velocidade = float(input('\nQual é a velocidade atual do carro em km/h? '))

if velocidade > 80: # condição simples
    print('Multado! Você excedeu o limite de 80km/h.')
    multa = (velocidade - 80) * 7
    print(f'Valor da multa: R$ {multa:,.2f}')

print('Tenha um bom dia! Dirija com segurança.\n')
