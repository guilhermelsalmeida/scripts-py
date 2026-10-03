# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5) # gera um número aleatório no intervalo escolhido.

print('\n')
print('=' * 60)
jogador = int(input('Adivinhe o número no qual estou pensando entre 0 e 5: '))
print('Processando...')
sleep(2)

if jogador == computador:
    print('Parabéns! Você adivinhou!')
else:
    print(f'Ops! Número errado. Eu pensei no número {computador}, e não no número {jogador}.')
print('=' * 60)
print('\n')
