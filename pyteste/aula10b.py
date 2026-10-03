nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Média: {media:.1f}')

# if media >= 7.0:
#    print('Sua média foi boa. Parabéns!')
# else:
#    print('Sua média foi ruim. Estude mais.')

print('Sua média foi boa. Parabéns!!!' if media >= 7.0 else 'Sua média foi ruim. Estude mais.') # Condicional simplificada
