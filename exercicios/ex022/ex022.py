# Crie um programa que leia o nome completo de uma pessoa e mostre: 1) O nome com todas as letras maiúsculas; 2) O nome com todas minúsculas; 3) Quantas letras ao todo (sem considerar espaços); e 4) Quantas letras tem o primeiro nome.

nome = str(input('\nDigite seu nome completo: '))
nome = nome.strip() # elimina os espaços antes e depois.

print('\nAnalisando seu nome...')
print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
print(f'Seu nome tem, ao todo, {len(nome) - nome.count(' ')} letras.')
# print(f'Seu primeiro nome tem {nome.find(' ')} letras.')

separa = nome.split() # transforma em uma lista
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')
