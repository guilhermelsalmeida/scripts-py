# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('\nDigite o ângulo: '))
ang = radians(angulo)
seno = sin(ang)
cosseno = cos(ang)
tangente = tan(ang)

print(f'\nO ângulo de {angulo:.0f}° tem:\nSENO = {seno:,.2f}\nCOSSENO = {cosseno:,.2f}\nTANGENTE = {tangente:,.2f}.')
