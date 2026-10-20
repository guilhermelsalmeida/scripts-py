# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print(f'\n{' GERADOR DE PA ':-^30}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
contador = 1
total_termos = 0
mais_termos = 10

while mais_termos != 0:
    total_termos += mais_termos
    while contador <= total_termos:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('| PAUSA\n')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Fim da PA | Total de termos mostrados: {total_termos}\n')
