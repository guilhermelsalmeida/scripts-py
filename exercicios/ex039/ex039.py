# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. O programa também deve mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input('\nDigite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'\nQuem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
print('-' * 50)

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!\n')
elif idade < 18:
    anos_faltando = 18 - idade
    print(f'Ainda faltam {anos_faltando} anos para o alistamento.')
    ano_alistamento = ano_atual + anos_faltando
    print(f'Seu alistamento será em {ano_alistamento}.\n')
else:
    anos_passados = idade - 18
    print(f'Você já deveria ter se alistado há {anos_passados} anos.')
    print(f'Seu alistamento foi em {ano_atual - anos_passados}.\n')
