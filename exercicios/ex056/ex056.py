# Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre: 1) A média de idade do grupo; 2) Qual é o nome do homem mais velho; e 3) Quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idadeh = 0
nome_hvelho = ''
tot_mulher20 = 0

print('\n')
for pessoa in range(1, 5):
    print(f'{f' {pessoa}ª PESSOA ':-^25}')
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idadeh = idade
        nome_hvelho = nome
    if sexo in 'Mm' and idade > maior_idadeh:
        maior_idadeh = idade
        nome_hvelho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 += 1

print(f'{f' ANÁLISE DO GRUPO ':-^40}')
print(f'Média de idade: {soma_idade / 4}')
print(f'Homem mais velho: {nome_hvelho} | Idade: {maior_idadeh} anos')
print(f'Mulheres menores de 20 anos: {tot_mulher20}\n')
