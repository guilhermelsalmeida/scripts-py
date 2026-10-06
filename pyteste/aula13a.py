# ESTRUTURAS DE REPETIÇÃO

# for c in range(0, 6, 2):
#    print(c)
# print('\nFIM\n')

# for c in range(3, 0, -1):
#    print(c)
#print('\nFIM')

# inicio = int(input('\nDe onde você quer começar a contar? '))
# fim = int(input('Até quanto você quer contar? '))
# passo = int(input('De quantos em quantos números você quer pular? '))

# for c in range(inicio, fim + 1, passo):
#    print(c)
# print('\nFIM\n')

soma = 0

for c in range(0, 3):
    print(c)
    numero = int(input('Digite um número: '))
    soma += numero # soma = soma + numero

print(f'\nSoma: {soma}')
print('FIM\n')
