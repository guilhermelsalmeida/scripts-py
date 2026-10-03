# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ‘Santo’.

cidade = input('\nEm que cidade você nasceu: ').strip()

print(f'\nSua cidade começa com SANTO? {cidade[:5].upper() == 'SANTO'}')
