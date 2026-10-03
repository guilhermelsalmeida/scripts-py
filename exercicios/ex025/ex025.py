# Crie um programa que leia o nome de uma pessoa e diga se ela tem ‘Silva’ no nome.

nome = input('\nDigite seu nome completo: ').strip()

print(f'Seu nome tem SILVA? {'silva' in nome.lower()}')
