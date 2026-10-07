# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# SOLUÇÃO 01
# soma = 0 # acumulador 
# for contador in range(1, 501):
#    if contador % 2 != 0 and contador % 3 == 0:
#        soma += contador # soma = soma + contador
# print(f'\nSoma: {soma}\n')

# SOLUÇÃO 02

soma = 0 # acumulador
cont = 0 # contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1

print(f'\nSoma: {soma} | Quantidade de números: {cont}\n')
