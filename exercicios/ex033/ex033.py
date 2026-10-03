# Faça um programa que leia três números inteiros e mostre qual é o maior e qual é o menor.

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# VERIFICANDO O MENOR NÚMERO
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3


# VERIFICANDO O MAIOR NÚMERO
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'\nMenor número: {menor}')
print(f'Maior número: {maior}\n')
