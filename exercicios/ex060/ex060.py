# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.

# SOLUÇÃO 01
# from math import factorial

# num = int(input('\nDigite um número para calcular o fatorial: '))
# fat = factorial(num)

# print(f'Fatorial de {num}: {fat}\n')

# SOLUÇÃO 02
# from time import sleep
# num = int(input('\nDigite um número para calcular o fatorial: '))

# contador = num
# fat = 1

# print(f'Calculando {contador}!...')
# sleep(1)

# while contador > 0:
#    print(f'{contador}', end='')
#    print(' x ' if contador > 1 else ' = ', end='')
#    fat *= contador # fat = fat * contador
#    contador -= 1 # contador = contador - 1
# print(f'{fat}\n')


# SOLUÇÃO 03
from time import sleep

num = int(input('\nDigite um número para calcular o fatorial: '))

fat = 1

print(f'Calculando {num}!...')
sleep(1)

for contador in range(num, 0, -1):
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fat *= contador

print(f'{fat}\n')
