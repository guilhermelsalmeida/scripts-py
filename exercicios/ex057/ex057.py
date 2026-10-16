# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('\nInforme seu sexo [M/F]: ').strip().upper()

while sexo not in ['M', 'F']:
    sexo = input('Dados inválidos. Por favor, informe seu sexo [M/F]: ').strip().upper()

print('-' * 55)
print(f'Sexo [{sexo}] registrado com sucesso!\n')
