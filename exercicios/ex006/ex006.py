# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

n = float(input('\nDigite um número: '))

print(f'\n{cores["fundobrancoletrapreta"]} Dobro de {n:.0f}: {n * 2:.0f} {cores["limpo"]}\n{cores["fundobrancoletrapreta"]} Triplo de {n:.0f}: {n * 3:.0f} {cores["limpo"]}\n{cores["fundobrancoletrapreta"]} Raiz quadrada de {n:.0f}: {n ** (1/2):.2f} {cores["limpo"]}\n')
# raizq = pow(n, 1/2) # A raiz quadrada também pode ser calculada usando a função pow(), que eleva o número a uma potência. Nesse caso, a base é n e a potência é 1/2.
