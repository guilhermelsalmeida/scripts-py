n1 = int(input('Digite um número: ')) # conversão direto na variável

print(type(n1))

n2 = input('Digite outro número: ')
n2 = int(n2) # conversão através de atualização da variável

print(type(n2))

print(n1 + n2) # soma usando diretamente as variáveis

s = n1 + n2
print('A soma vale', s)

print(f'A soma entre {n1} e {n2} é igual a {s}')