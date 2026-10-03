# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

numero = int(input('\nDigite um número: '))

print(f'\nAntecessor de {numero}: {cores["fundoamareloletrapreta"]} {numero - 1} {cores["limpo"]}\nSucessor de {numero}: {cores["fundoamareloletrapreta"]} {numero + 1} {cores["limpo"]}')
