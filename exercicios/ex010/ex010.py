# Crie um programa que leia quanto dinheiro, em real, uma pessoa tem na carteira e mostre quantos dólares e euros ela pode comprar. Considere US$ 1,00 = R$ 5,20 e € 1,00 = R$ 5.99.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

real = float(input(f'\n{cores["fundoamareloletrapreta"]} Quanto dinheiro você tem na carteira? {cores["limpo"]} R$ '))
dolar = real / 5.20
euro = real / 5.99

print(f'\nCom R$ {real:,.2f}, você pode comprar US$ {cores["verde"]}{dolar:,.2f}{cores["limpo"]} e € {cores["verde"]}{euro:,.2f}{cores["limpo"]}.')
