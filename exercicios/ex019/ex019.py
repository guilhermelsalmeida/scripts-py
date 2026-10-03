# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.

from random import choice

aluno1 = input('Aluno 01: ')
aluno2 = input('Aluno 02: ')
aluno3 = input('Aluno 03: ')
aluno4 = input('Aluno 04: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido foi: {choice(lista_alunos)}.')
