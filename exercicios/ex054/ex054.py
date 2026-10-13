# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores (considere a maioridade aos 21 anos).

from datetime import date

ano_atual = date.today().year

print('\n')

tot_maior = 0
tot_menor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    idade = ano_atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior.')
        tot_maior += 1
    else:
        print('Essa pessoa é menor.')
        tot_menor += 1
print(f'\nTotal de maiores: {tot_maior}')
print(f'Total de menores: {tot_menor}\n')
