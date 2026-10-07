# Crie um programa que faça o computador jogar Jokenpô (pedra, papel e tesoura) contra o usuário.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print(f'\n{' JOKENPÔ ':=^30}')
print('-' * 30)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-' * 30)

jogador = int(input('Qual é a sua jogada? '))

print('-' * 30)
print('JO')
sleep(1)

print('KEN')
sleep(1)

print('PÔ!')
sleep(1)

print('-' * 30)
print(f'''Computador jogou: {itens[computador]}
Jogador jogou: {itens[jogador]}''')
print('-' * 30)

if computador == 0: # Computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')

elif computador == 1: # Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    else:
        print('JOGADOR VENCEU!')

else: # Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    else:
        print('EMPATE!')

print('\n')
