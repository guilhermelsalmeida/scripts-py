# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Exemplo: Ana Maria de Souza; Primeiro nome – Ana; Último nome – Souza.

nome = input('\nDigite seu nome completo: ').strip()
nomef = nome.split()
print(f'Primeiro nome: {nomef[0]}')
print(f'Último nome: {nomef[len(nomef)-1]}')
