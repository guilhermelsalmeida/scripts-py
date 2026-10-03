# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status: abaixo de 18.5 (Abaixo do Peso), entre 18.5 e 25 (Peso Ideal), 25 até 30 (Sobrepeso), 30 até 40 (Obesidade) e acima de 40 (Obesidade Mórbida).

nome = input('\nDigite o nome: ').strip().capitalize()
peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))
imc = peso / (altura ** 2)

print('-' * 65)
print(f'Nome: {nome} | Peso: {peso:.2f}kg | Altura: {altura:.2f}m | IMC: {imc:.1f}')

if imc < 18.5:
    print('Status: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Status: PESO IDEAL')
elif 25 <= imc < 30:
    print('Status: SOBREPESO')
elif 30 <= imc < 40:
    print('Status: OBESIDADE')
else:
    print('Status: OBESIDADE MÓRBIDA')

print('-' * 65)
print('FONTE: Ministério da Saúde - Brasil\n')
