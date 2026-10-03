# import math
from math import sqrt, ceil, floor
# Não precisa mais referenciar math, quando importa diretamente a função.

num = float(input('\nDigite um número: '))
# raizq = math.sqrt(num) # extrai a raiz quadrada.
raizq = sqrt(num)

print(f'\nA raiz quadrada de {num:.0f} é igual a {raizq:.2f}')
print(f'\nA raiz quadrada de {num:.0f} é igual a {ceil(raizq)}') # arredonda para cima
print(f'\nA raiz quadrada de {num:.0f} é igual a {floor(raizq)}') # arredonda para baixo
