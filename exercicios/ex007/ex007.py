# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

nome = input('\nDigite o nome do aluno: ')
nota1 = float(input('\nDigite a primeira nota do aluno: '))
nota2 = float(input('\nDigite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

print(f'\n{cores["fundoamareloletrapreta"]} Média de {nome}: {media:.2f} {cores["limpo"]}\n')

# As variáveis em Python aceitam acentos e caracteres especiais, mas é uma boa prática evitar.
