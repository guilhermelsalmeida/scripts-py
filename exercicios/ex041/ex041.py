# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: até 9 anos (Mirim), até 14 anos (Infantil), até 19 anos (Júnior), até 25 anos (Sênior) e acima de 25 anos (Master).

from datetime import date

ano_nasc = int(input('\nDigite o ano de nascimento: '))
idade = date.today().year - ano_nasc

print('-' * 40)
print(f'Idade do atleta: {idade} anos')

if idade <= 9:
    print('Categoria: MIRIM\n')
elif idade <= 14:
    print('Categoria: INFANTIL\n')
elif idade <= 19:
    print('Categoria: JÚNIOR\n')
elif idade <= 25:
    print('Categoria: SÊNIOR\n')
else:
    print('Categoria: MASTER\n')
