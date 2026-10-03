# Escreva um programa que leia um valor em metros e o exiba convertido em alqueires, hectares, milhas, quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

valor = float(input('\nDigite uma distância (em metros): '))

print(f'\n{cores["fundobrancoletrapreta"]} {valor:.0f} metros equivalem a: {cores["limpo"]}')
print(f'\n{valor / 24200:.6f} alqueires;') # aqui foi considerado o alquire paulista, que equivale a 24200 metros quadrados.
print(f'{valor / 10000:.6f} hectares;')
print(f'{valor / 1609.34:.6f} milhas;')
print(f'{valor / 1000:.6f} quilômetros;')
print(f'{valor / 100:.6f} hectômetros;')
print(f'{valor / 10:.6f} decâmetros;')
print(f'{valor * 10:.6f} decímetros;')
print(f'{valor * 100:.6f} centímetros; e')
print(f'{valor * 1000:.6f} milímetros.\n')
