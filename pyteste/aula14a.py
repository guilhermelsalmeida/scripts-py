# ESTRUTURA WHILE

# contador = 1 # diferente do for, é necessário criar uma variável contador antes do while
# while contador <= 3:
#    print(contador, end=' ')
#    contador = contador + 1  # ou contador += 1
# print("| Fim da contagem!\n")

# resposta = 'S'
# while resposta == 'S':
#    numero = int(input('Digite um valor: '))
#    resposta = input('Quer continuar: ').strip().upper()
# print('FIM\n')

# numero = 1
# tot_par = tot_impar = 0
# while numero != 0:
#    numero = int(input('Digite um número: '))
#    if numero != 0:
 #       if numero % 2 == 0:
 #           tot_par += 1
 #       else:
 #           tot_impar += 1
# print(f'\nTotal de números pares: {tot_par}')
# print(f'Total de números ímpares: {tot_impar}')
# print('FIM\n')

sexo = input("\nInforme seu sexo [M/F]: ").strip().upper()

while sexo not in ["M", "F"]:
    sexo = input("Dados inválidos. Por favor, informe seu sexo [M/F]: ").strip().upper()

print(f"Sexo [{sexo}] registrado com sucesso!\n")
