# Criar um jogo de "Par ou Ímpar" contra o computador, que só é encerrado quando o jogador perder, mostrando ao final o total de vitórias consecutivas.

from random import randint

print(f'\n{' PAR OU ÍMPAR ':-^40}')

vitoria = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in ['P', 'I']:
        tipo = input('Par ou ímpar [P/I]? ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'Total: {total}', end=' | ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu.')
            break
    else:
        if total % 2 != 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu.')
            break
    print('Vamos jogar novamente...')

print('-' * 40)
print('Game Over')
print(f'Você venceu {vitoria} vezes.\n')
