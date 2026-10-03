cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

algo = input('\nDigite algo: ')

print(f'O tipo primitivo desse valor é {cores["verde"]}{type(algo)}{cores["limpo"]}')

# TESTE SE PODE SER OUTRA COISA
print(f'Só há espaços? {cores["verde"]}{algo.isspace()}{cores["limpo"]}')
print(f'É um número? {cores["verde"]}{algo.isnumeric()}{cores["limpo"]}')
print(f'É alfabético? {cores["verde"]}{algo.isalpha()}{cores["limpo"]}')
print(f'É alfanumérico? {cores["verde"]}{algo.isalnum()}{cores["limpo"]}')
print(f'Está em maiúsculas? {cores["verde"]}{algo.isupper()}{cores["limpo"]}')
print(f'Está em minúsculas? {cores["verde"]}{algo.islower()}{cores["limpo"]}')
print(f'Está capitalizada? {cores["verde"]}{algo.istitle()}{cores["limpo"]}\n') # a primeira letra maiúscula

# Esses testes são úteis para validar dados de entrada, como senhas, nomes de usuário, etc.
