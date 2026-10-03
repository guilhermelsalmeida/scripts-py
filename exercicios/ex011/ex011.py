# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

cores = {'limpo': '\033[m', 'verde': '\033[1;32m', 'vermelho': '\033[1;31m', 'fundoamareloletrapreta': '\033[1;30;43m', 'fundobrancoletrapreta': '\033[1;30;47m'}

largura = float(input('\nDigite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta_necessaria = area / 2

print(f'\nA área da parede é de {cores["verde"]}{area:,.2f}m²{cores["limpo"]}.')
print(f'A quantidade de tinta necessária para pintar a parede é de {cores["vermelho"]}{tinta_necessaria:,.2f}{cores["limpo"]} litros.\n')
