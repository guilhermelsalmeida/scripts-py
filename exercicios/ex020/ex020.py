# Um professor quer sortear a ordem de apresentação de trabalhos dos seus quatro alunos. Faça um programa que leia o nome dos alunos e mostre a ordem sorteada.

import random

aluno1 = input('\nAluno 01: ')
aluno2 = input('Aluno 02: ')
aluno3 = input('Aluno 03: ')
aluno4 = input('Aluno 04: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_alunos)

print('\nA ordem de apresentação será: ')
# for i, aluno in enumerate(lista_alunos, start=1):
#    print(f'{i}º - {aluno}')

print(lista_alunos)
