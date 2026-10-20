# Crie um programa que leia dois valores e mostre um menu na tela (1) somar; 2) multiplicar; 3) maior; 4) novos números; 5) sair do programa). Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

num1 = int(input('\nDigite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
print('-' * 30)

opcao = 0
while opcao != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR''')
    print('-' * 30)
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'Soma: {num1} + {num2} = {soma}')
    elif opcao == 2:
        print(f'Multiplicação: {num1} × {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Maior: {maior}')
    elif opcao == 4:
        print('Informe os números novamente.')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')
    sleep(2)
    print('-' * 30)

print('Fim do Programa.\n')
