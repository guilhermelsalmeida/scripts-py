# Crie um programa que leia duas notas de um aluno e calcule sua média. Exiba uma mensagem no final de acordo com a média atingida: abaixo de 5.0 (reprovado), entre 5.0 e 6.9 (recuperação) ou 7.0 ou superior (aprovado).

nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('-' * 30)
print(f'Média: {media:.1f}')

if media < 5:
    print('Status: REPROVADO\n')
elif 5 <= media < 7:
    print('Status: RECUPERAÇÃO\n')
else:
    print('Status: APROVADO\n')
