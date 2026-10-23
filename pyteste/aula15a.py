# O COMANDO BREAK E AS ESTRUTURAS DE REPETIÇÃO.

# contador = 1

# while contador <= 10:
#    print(contador, end=' ')
#    contador += 1
# print('| ACABOU\n')


# num = soma = 0
# while num != 999: # uso de flag (999)
#    num = int(input('\nDigite um número: '))
#    if num != 999:
#        soma += num
# print(f'\nSoma: {soma}\n')



soma = 0
while True:
    num = int(input('\nDigite um número: '))
    if num == 999:
        break
    soma += num
print(f'\nSoma: {soma}\n')
