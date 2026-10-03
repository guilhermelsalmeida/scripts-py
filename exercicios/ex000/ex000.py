cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

print('Olá, Mundo!')
print('7' + '4') # o + funciona melhor
print('Olá', 5) # a vírgula funciona melhor


#VARIÁVEIS

# No Python, toda variável é um objeto e pode receber valores.

nome = ' Guilherme '
idade = '33'
peso = '74'

print(f'\nNome: {cores["fundobrancoletrapreta"]}{nome}{cores["limpo"]} | Idade: {idade} | Peso: {peso}')

nome2 = input('Qual é o seu nome? ')
# idade2 = input('Quantos anos você tem? ')
# peso2 = input('Qual é o seu peso? ')

print(f'\nOlá, {nome2}! Prazer em te conhecer!')

dia = input('Qual dia você nasceu? ')
mes = input('Em que mês você nasceu? ')
ano_nasc = input('Em que ano você nasceu? ')

print(f'Você nasceu em {dia}/{mes}/{ano_nasc}, Correto?')

n1 = input('Digite um número: ')
n1 = int(n1)
n2 = input('Digite outro número: ')
n2 = int(n2)

print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}, certo?')