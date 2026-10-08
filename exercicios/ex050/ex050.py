# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
print('\n')
for c in range(1, 7):
    num = int(input(f'{c}º Número: '))
    if num % 2 == 0:
        soma += num
print(f'Soma dos números pares: {soma}\n')
