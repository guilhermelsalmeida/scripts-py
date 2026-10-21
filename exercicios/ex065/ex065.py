# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'S'
media = soma = qtd_valores = maior = menor = 0

while resposta in 'Ss':
    num = int(input('\nDigite um número: '))
    soma += num
    qtd_valores += 1
    if qtd_valores == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = input('Quer continuar [S/N]? ').strip().upper()[0]

media = soma / qtd_valores

print(f'\nNúmeros digitados: {qtd_valores} | Média: {media}')
print(f'Maior valor: {maior} | Menor valor: {menor}\n')
