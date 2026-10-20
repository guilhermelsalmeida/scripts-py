# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(f'\n{' GERADOR DE PA ':-^30}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

print('| FIM.\n')
