# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8.

print(f'\n{' SEQUÊNCIA DE FIBONACCI ':-^40}')

num_termos = int(input('Quantos termos você quer mostrar? '))

termo1 = 0
termo2 = 1

print('-' * 40)
print(f'{termo1} -> {termo2}', end='')

contador = 3

while contador <= num_termos:
    termo3 = termo1 + termo2
    print(f' -> {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1

print(' | FIM\n')
