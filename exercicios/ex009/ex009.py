# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

num = int(input('\nDigite um número inteiro para ver sua tabuada: '))

print('\n')
print(f'{cores["verde"]}-{cores["limpo"]}' * 15)
print(f'{cores["vermelho"]}Tabuada do {num}:{cores["limpo"]}')
for i in range(1, 11):
    print(f'{cores["fundobrancoletrapreta"]} {num} × {i:2} = {num * i} {cores["limpo"]}')
print(f'{cores["verde"]}-{cores["limpo"]}' * 15)
print('\n')
