# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo (divisível apenas por 1 e por ele mesmo).

numero = int(input('\nDigite um número: '))
total = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\033[m| O número {numero} foi divisível {total} vezes.', end=' ')

if total == 2:
    print('Por isso, é um número primo.\n')
else:
    print('Por isso, não é um número primo.\n')
