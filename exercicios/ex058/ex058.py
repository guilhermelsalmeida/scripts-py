# Melhore o jogo do desafio 028 (no qual o computador pensa em um número de 0 a 10), só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)

print('\nSou seu computador. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('-' * 65)

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais, tente mais uma vez.')
        else:
            print('Menos, tente mais uma vez.')

print(f'Você acertou com {palpites} palpites. Parabéns!\n')
