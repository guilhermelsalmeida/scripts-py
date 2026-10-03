# Desenvolva um programa que leia os comprimentos de três retas e diga ao usuário se podem ou não formar um triângulo.

reta1 = float(input('\nDigite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

# Para que três retas possam formar um triângulo, a soma de dois lados deve ser maior que o terceiro lado.

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('As retas podem formar um triângulo.\n')
else:
    print('As retas não podem formar um triângulo.\n')
