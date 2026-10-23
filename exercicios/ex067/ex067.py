# Mostrar a tabuada de vários números, para cada número digitado pelo usuário, um de cada vez, interrompendo o programa quando o número digitado for negativo.

print(f'\n{' TABUADA ':-^40}')

while True:
    num = int(input('''Quer ver a tabuada de qual valor?
Número negativo finaliza: '''))
    print('-' * 40)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} × {c:>2} = {num * c}')
    print('-' * 40)

print('Fim do programa.\n')
