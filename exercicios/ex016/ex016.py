# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua parte inteira. Exemplo: se for digitado 6.127, será exibido 6.

# import math
# from math import trunc

num = float(input('\nDigite um número: '))
# parteintnum = math.trunc(num)
# parteintnum = trunc(num)

print(f'\nO número digitado foi {num} e a parte inteira é {int(num)}.')
