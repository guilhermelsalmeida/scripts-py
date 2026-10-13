# Faça um programa que leia o peso de cinco pessoas e, no final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0

print('\n')
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'\nMaior peso lido: {maior_peso:.2f}Kg.')
print(f'Menor peso lido: {menor_peso:.2f}Kg.\n')
