# Refaça o Desafio 09 (tabuada de um número digitado pelo usuário), mostrando a tabuada de forma simplificada utilizando um laço for.

numero = int(input('\nDigite um número para ver sua tabuada: '))

print(f'''{'-' * 12}
{'TABUADA':^12}
{'-' * 12}''')

for i in range(1, 11):
    print(f'{numero} × {i:2} = {numero * i}')

print(f'{'-' * 12}\n')
