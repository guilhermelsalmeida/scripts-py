# Faça um programa que leia os comprimentos do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catop = float(input('\nDigite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
# hip = (catop ** 2 + catad ** 2) ** (1/2)
hip = hypot(catop, catad)

print(f'\nCom o cateto oposto medindo {catop:.2f} e o cateto adjacente medindo {catad:.2f}, a hipotenusa mede {hip:.2f}.')
