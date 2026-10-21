# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada (flag). No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print(f'\n{' SOMATÓRIO ':-^45}')

num = int(input('Digite um número [999 para parar]: '))
print('-' * 45)
num = soma = contador = 0

while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
    print('-' * 45)

print(f'Total de números digitados: {contador} | Soma: {soma}\n')
