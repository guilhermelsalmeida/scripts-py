# OPERADORES ARITMÉTICOS

nome = input('Digite seu nome: ')
print(f'Olá, {nome}! Prazer em te conhecer!')
print(f'Olá, {nome:20}! Prazer em te conhecer!') # formatação de string com 20 caracteres de largura
print(f'Olá, {nome:>20}! Prazer em te conhecer!') # 20 caracteres de largura, alinhado à direita
print(f'Olá, {nome:<20}! Prazer em te conhecer!') # 20 caracteres de largura, alinhado à esquerda
print(f'Olá, {nome:^20}! Prazer em te conhecer!') # 20 caracteres de largura, centralizado
print(f'Olá, {nome:=^20}! Prazer em te conhecer!') # 20 caracteres de largura, centralizado, preenchido com igual

print('\n')
n1 = int(input('Digite um número: '))
n2 = input('Digite outro número: ')
n2 = int(n2) # convertendo a variavel para inteiro separadamente
soma = n1 + n2
subtracao = n1 - n2

print('A soma vale {} e a subtração vale {}'.format(soma, subtracao), end='. ') # usando o método da função format. end='' não quebra a linha
print(f'A multiplicação vale {n1 * n2}.\nA divisão vale {n1 / n2:.3f}, a divisão inteira vale {n1 // n2} e {n1} elevado a {n2} vale {n1 ** n2}') # \n quebra a linha