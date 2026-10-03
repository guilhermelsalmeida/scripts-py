# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão (1 para binário, 2 para octal e 3 para hexadecimal).

numero = int(input('\nDigite um número inteiro: '))

print('''\nEscolha a base de conversão:
[ 1 ] Cnverter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'\n{numero} convertido para BINÁRIO = {bin(numero)[2:]}\n') # [2:] remove o prefixo '0b' da representação binária
elif opcao == 2:
    print(f'\n{numero} convertido para OCTAL = {oct(numero)[2:]}\n') # [2:] remove o prefixo '0o' da representação octal
elif opcao == 3:
    print(f'\n{numero} convertido para HEXADECIMAL = {hex(numero)[2:]}\n') # [2:] remove o prefixo '0x' da representação hexadecimal
else:
    print('\nOpção inválida! Tente novamente.\n')
