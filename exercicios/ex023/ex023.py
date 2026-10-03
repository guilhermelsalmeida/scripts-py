# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Exemplo: Digite um número: 1834; Unidade: 4; Dezena: 3; Centena: 8; e Milhar: 1.

num = int(input('\nDigite um número de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'\nAnalisando o número {num}...')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
