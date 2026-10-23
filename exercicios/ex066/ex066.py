# Ler vários números inteiros até que o usuário digite o flag 999. No final, mostrar quantos números foram digitados e a soma entre eles (desconsiderando o flag).

# SOLUÇÃO 01
# num = soma = 0

# while num != 999:
#    num = int(input('\nDigite um número [999 finaliza]: '))
#    if num != 999:
#        soma += num

# print(f'\nFim do programa | Soma: {soma}\n')


# SOLUÇÃO 02
soma = contador = 0

while True:
    num = int(input('\nDigite um número [999 finaliza]: '))
    if num == 999:
        break
    contador += 1
    soma += num

print(f'\nFim do programa | Total de números digitados: {contador} | Soma: {soma}\n')
