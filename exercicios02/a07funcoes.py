# A principal finalidade das funções é permitir a reutilização de código. Uma função é um bloco de código que realiza uma tarefa específica e pode ser chamada várias vezes em diferentes partes do programa, evitando a repetição de código e facilitando a manutenção. Exemplo: diferentes alíquotas de imposto aplicadas a diferentes produtos ou serviços.

def pula_linha():
    print('\n') # função que imprime uma linha em branco

lista_precos = [1500, 1000, 800, 2000]

def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.1
        imposto = preco * taxa
        imposto_total += imposto # imposto_total = imposto_total + imposto
    return imposto_total # return: interrompe a execução da função; então, deve ser a última linha da função.

imposto_lista1 = calcular_imposto(lista_precos)
print(f'Imposto total Lista 01: R$ {imposto_lista1:,.2f}')

lista2_precos = [500, 4000, 3200, 2600, 1000]

imposto_lista2 = calcular_imposto(lista2_precos)
print(f'Imposto total Lista 02: R$ {imposto_lista2:,.2f}')

pula_linha()


# Funções podem ser criadas para coisas bem simples. Deve-se ter cuidado para não nomear uma função com o mesmo nome de uma variável. Funções podem funcionar sem parâmetros.
# Funções sem parâmetros podem ser úteis para realizar tarefas que não dependem de dados externos. Não retornam valores

def saudacoes():
    print('Olá! Seja bem-vindo!')

saudacoes()
pula_linha()

# Geralmente funções cumprem 1 só objetivo. É possível chamar funções dentro de funções.
# Variáveis definidas dentro de funções são locais e não podem ser acessadas fora da função.


# EXERCÍCIO: Par ou ímpar

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

total_par = 0
soma_par = 0
total_impar = 0
soma_impar = 0
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_numeros)

for numero in lista_numeros:
    resultado = par_ou_impar(numero)
    if resultado == 'PAR':
        total_par += 1
        soma_par += numero
    else:
        total_impar += 1
        soma_impar += numero

print(f'Total de pares: {total_par}')
print(f'Soma dos pares: {soma_par}')
print(f'Total de ímpares: {total_impar}')
print(f'Soma dos ímpares: {soma_impar}')