# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela: "O primeiro valor é maior", "O segundo valor é maior" ou "Não existe valor maior, os dois são iguais".

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('-' * 35)
    print(f'O primeiro valor [{num1}] é maior.\n')
elif num2 > num1:
    print('-' * 35)
    print(f'O segundo valor [{num2}] é maior.\n')
else:
    print('-' * 60)
    print(f'Não há valor maior. Os dois são iguais: [{num1}] = [{num2}]\n')
