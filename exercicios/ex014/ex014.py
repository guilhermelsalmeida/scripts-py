# Escreva um programa que converta uma temperatura digitada em graus célsius (°C) e converta para fahrenheit (°F).

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

celsius = float(input(f'\n{cores["fundoamareloletrapreta"]} Digite a temperatura em °C: {cores["limpo"]} '))
fahrenheit = (celsius * 9/5) + 32

print(f'\nA temperatura de {cores["fundobrancoletrapreta"]} {celsius:.2f}°C {cores["limpo"]} corresponde a {cores["verde"]}{fahrenheit:.2f}°F{cores["limpo"]}.\n')
